
import os

# Trading mode
LIVE_MODE = os.getenv("LIVE_MODE", "false").lower() == "true"

# API keys
COINBASE_API_KEY = os.getenv("COINBASE_API_KEY")
COINBASE_API_SECRET = os.getenv("COINBASE_API_SECRET")
