
from data.market_intel import fetch_perplexity_summary

def test_fetch_summary():
    result = fetch_perplexity_summary("Bitcoin")
    assert isinstance(result, str)
