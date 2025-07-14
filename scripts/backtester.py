
from data.market_intel import fetch_perplexity_summary
from data.numerology_checker import check_numerology
from data.astrology_fetcher import fetch_astrology_data
from core.astro_scoring import score_astrological_alignment

def run_backtest():
    print("Starting backtest...")
    for date in ["2022-08-08", "2023-11-11"]:
        print(f"Simulating date: {date}")
        market_sentiment = fetch_perplexity_summary("crypto news")
        astro_data = fetch_astrology_data()
        numerology = check_numerology(date)
        score = score_astrological_alignment(astro_data)
        print(f"🪐 Astro Score: {score}, 🔢 Numerology: {numerology}")
