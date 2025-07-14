
# AstroQuant 🔮📈

AstroQuant is an autonomous AI trading agent that fuses real-time market intelligence with esoteric wisdom (astrology, numerology, and life path alignment) to generate and execute trades via Coinbase.

## 🔧 Features
- Perplexity.AI-based market sentiment parsing
- Astrology signal alignment using public APIs
- Numerology and repeating pattern signal timing
- Trade signal synthesis and auto-execution
- Backtest mode for validating strategy
- Streamlit dashboard for visibility and control

## 📦 Project Structure
```
AstroQuant/
├── core/               # Core logic for signal generation and trade execution
├── data/               # Data fetchers: market, astrology, numerology
├── scripts/            # Scheduler and backtester logic
├── utils/              # Logging and config management
├── main.py             # Entry point
├── requirements.txt    # Dependencies
└── streamlit_app.py    # Dashboard
```

## 🚀 Usage

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Streamlit dashboard:
```bash
streamlit run streamlit_app.py
```

3. Extend modules:
- `market_intel.py` to add advanced sentiment parsing (e.g., using Selenium)
- `astrology_fetcher.py` to use `flatlib` or API for moon phases & retrogrades
- `numerology_checker.py` to use life path and time signals

## 🧙 Inspired By:
- Astro-trading principles
- Quantitative finance
- Conscious wealth generation

---

**Note**: For best performance, consider headless browser automation with Selenium to pull full Perplexity.AI results.


---

## 🧪 Testing & Reporting

### 📦 Run Tests with Pytest
```bash
pytest
```

### 📊 View Results with Allure
Install Allure CLI:

```bash
brew install allure    # macOS
# OR
scoop install allure   # Windows
```

Then run:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

### ✅ CI/CD via GitHub Actions
A GitHub Actions workflow is included in `.github/workflows/ci.yml` to automatically:
- Install dependencies
- Run tests with pytest
- Generate and upload Allure test report

---

## 🐳 Docker Usage

### Build & Run Locally

```bash
docker build -t astroquant .
docker run -p 8501:8501 --env-file .env astroquant
```

---

## 🔐 Env Setup
Use the included `.env` template and load it with:
```bash
pip install python-dotenv
```
