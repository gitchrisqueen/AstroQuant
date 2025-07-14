
from utils.config import LIVE_MODE

def place_market_order(symbol, side, amount):
    if LIVE_MODE:
        print(f"[LIVE MODE] Executing {side.upper()} market order for {amount} {symbol}")
        # Add real API call logic here
    else:
        print(f"[PAPER MODE] Simulated {side.upper()} order for {amount} {symbol}")
