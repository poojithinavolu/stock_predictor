from flask import Flask, render_template, request, jsonify
from datetime import datetime, date
import yfinance as yf
import pandas as pd
from prophet import Prophet
from transformers import pipeline

app = Flask(__name__)

# Initialize the LLM pipeline (GPT-2 Medium for text generation)
llm_generator = pipeline('text-generation', model='gpt2-medium', framework='pt')

@app.route('/')
def index():
    return render_template('index.html', date=date)

@app.route('/forecast', methods=['POST'])
def forecast():
    ticker     = request.form.get('ticker', '').strip().upper()
    start_date = request.form.get('start_date') or '2020-01-01'
    end_date   = request.form.get('end_date')   or datetime.today().strftime('%Y-%m-%d')
    days       = int(request.form.get('forecast_days', 30))

    if not ticker:
        return "Error: ticker required", 400

    # Fetch historical data
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        return f"No data for '{ticker}' in {start_date}–{end_date}", 400

    # Prepare DataFrame for Prophet: use only the 'Close' series
    df = data['Close'].reset_index()
    df.columns = ['ds', 'y']
    df['ds'] = pd.to_datetime(df['ds'])

    # Fit Prophet model
    m = Prophet(daily_seasonality=True)
    m.fit(df)

    # Forecast
    future   = m.make_future_dataframe(periods=days)
    forecast = m.predict(future)

    # Split historical vs. forecast
    last = df['ds'].max()
    hist = df[df['ds'] <= last]
    fut  = forecast[forecast['ds'] > last]

    hist_dates  = hist['ds'].dt.strftime('%Y-%m-%d').tolist()
    hist_prices = hist['y'].tolist()
    fut_dates   = fut['ds'].dt.strftime('%Y-%m-%d').tolist()
    fut_prices  = fut['yhat'].round(2).tolist()

    # LLM narrative
    prompt = (
        f"As an expert financial analyst, summarize the stock price forecast for {ticker} "
        f"based on historical data through {end_date} and a {days}-day outlook."
    )
    resp     = llm_generator(prompt, max_length=150, num_return_sequences=1)
    analysis = resp[0]['generated_text']

    return render_template('result.html',
                           ticker     = ticker,
                           hist_dates = hist_dates,
                           hist_prices= hist_prices,
                           fut_dates  = fut_dates,
                           fut_prices = fut_prices,
                           analysis   = analysis)

@app.route('/ask', methods=['POST'])
def ask():
    data     = request.get_json()
    question = data.get('question','').strip()
    if not question:
        return jsonify(answer="Please enter a question."), 400

    prompt = (
        "As a knowledgeable financial advisor, answer the following question:"
        f"Question: {question} Answer:"
    )
    resp   = llm_generator(prompt, max_length=100, num_return_sequences=1)
    answer = resp[0]['generated_text'].replace(prompt,'').strip()
    return jsonify(answer=answer)

if __name__ == '__main__':
    app.run(debug=True)