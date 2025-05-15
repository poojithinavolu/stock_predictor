```markdown
# 📈 Financial Forecasting Assistant

The **Financial Forecasting Assistant** is a Flask-based web application that combines **stock price forecasting**, **interactive charting**, and **LLM-powered financial analysis**. Users can enter a stock ticker, select a date range, and view a forecast of future stock prices powered by **Meta's Prophet** model. It also includes an **AI advisor chatbot** (powered by GPT-2) to answer user queries in natural language.

---

## 🚀 Features

- 📊 Forecast stock prices using [Meta Prophet](https://facebook.github.io/prophet/)
- 🧠 AI-generated forecast analysis with GPT-2
- 💬 Ask finance-related questions via a built-in LLM-powered chatbot
- 📅 Custom date range and forecast period input
- 📈 Interactive line charts powered by [Chart.js](https://www.chartjs.org/)
- 🌐 Simple and responsive frontend using Flask templates and vanilla JavaScript

---

## 📌 Use Case

This app is ideal for:
- Beginner to intermediate finance enthusiasts who want quick and simple visual forecasting.
- Students and educators building prototypes that integrate AI, finance, and data visualization.
- Developers exploring how to integrate LLMs and time-series forecasting into web apps.

---

## 🛠️ Tech Stack

| Layer        | Technology               |
|--------------|---------------------------|
| Backend      | Python, Flask             |
| Forecasting  | Prophet (by Meta)         |
| Financial Data | yFinance                |
| AI/NLP       | HuggingFace Transformers (`gpt2-medium`) |
| Frontend     | HTML, CSS, JavaScript     |
| Charting     | Chart.js                  |

---

## 📁 Project Structure

```

financial-forecasting-assistant/
├── app.py                # Main Flask backend
├── templates/
│   ├── index.html        # Input form for forecasting
│   └── result.html       # Results page with charts and analysis
├── static/
│   └── style.css         # (Optional) custom styles
├── requirements.txt      # Python dependencies
└── README.md             # This file

````

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/financial-forecasting-assistant.git
cd financial-forecasting-assistant
````

### 2. Create and Activate a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, manually install:

```bash
pip install flask pandas prophet yfinance transformers torch
```

> 🧠 **Note**: `prophet` requires `pystan`. If you encounter installation issues, try:
>
> ```bash
> pip install pystan==2.19.1.1 prophet
> ```

---

## ▶️ Running the App

Once dependencies are installed and the virtual environment is activated:

```bash
python app.py
```

Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## 🧠 How It Works

1. **User Input**:

   * Enter a stock ticker (e.g., `AAPL`, `GOOGL`).
   * Select start & end dates.
   * Choose forecast days (e.g., 30 days ahead).

2. **Data Fetching**:

   * Historical data is pulled from Yahoo Finance using `yfinance`.

3. **Forecasting**:

   * A time series is built from the closing prices.
   * Prophet generates a future forecast based on trends and seasonality.

4. **Visualization**:

   * Historical and forecast data are plotted using Chart.js.

5. **Narrative Summary**:

   * GPT-2 generates a financial narrative describing the forecast.

6. **Ask Questions**:

   * Users can interact with a chatbot and get financial advice/insights using GPT-2.

---

## ✨ Example Screenshots

<details>
<summary>📷 Forecasting Page</summary>

![Forecast Form](https://via.placeholder.com/800x400?text=Form+Example)

</details>

<details>
<summary>📷 Forecast Output & Chatbot</summary>

![Forecast Output](https://via.placeholder.com/800x400?text=Chart+and+Chatbot)

</details>

> Replace with actual screenshots after deploying locally.

---

## 🤖 Notes on AI Components

* **Text Generation**: Uses the `gpt2-medium` model from HuggingFace's `transformers` library.
* **Forecast Summary**: LLM generates a human-readable analysis of the forecast.
* **Q\&A**: The LLM responds to questions in a financial advisory tone.

> ⚠️ GPT-2 is a general-purpose model and may hallucinate. It’s used here for demo purposes. For more robust answers, consider using GPT-3.5/GPT-4 via OpenAI API or similar.

---

## 🧪 Sample Prompts

* “What does the future look like for TSLA?”
* “Why did Apple’s price fluctuate in 2022?”
* “Will Amazon's price rise next month?”
* “Explain the forecast trend in layman’s terms.”

---

## 🧼 To-Do & Improvements

* [ ] Add user authentication
* [ ] Allow saving/exporting forecasts as PDF
* [ ] Upgrade to OpenAI API or Gemini for richer answers
* [ ] Improve PDF-based financial report uploads
* [ ] Make UI responsive (Bootstrap/Tailwind)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

* ⭐ Star this repository
* 📥 Fork and clone
* ✅ Submit pull requests with improvements or bug fixes

---

## 🙋 FAQ

**Q: Do I need an API key to run this?**
A: No. It uses public models like GPT-2 and yFinance which don’t require API keys.

**Q: Can I use this for crypto?**
A: Not directly. `yfinance` supports traditional stocks. You’ll need to modify the data source for crypto.

**Q: Can this be deployed?**
A: Yes! Deploy it to Heroku, Render, or Replit. Let me know if you need a `Procfile` or deployment guide.

---

## 👨‍💻 Author

**Your Name**
[GitHub](https://github.com/poojithinavolu/) • [LinkedIn](https://www.linkedin.com/in/poojith-inavolu-469320277/)

---
