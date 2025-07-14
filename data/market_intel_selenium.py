
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def fetch_perplexity_sentiment(query):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(f"https://www.perplexity.ai/search?q={query.replace(' ', '+')}")
        time.sleep(3)
        results = driver.find_elements(By.CLASS_NAME, "thread-block")
        summary = "\n".join([r.text for r in results[:3]])
    finally:
        driver.quit()

    return summary or "No content found"
