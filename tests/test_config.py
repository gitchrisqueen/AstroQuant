
from utils import config

def test_live_mode_flag():
    assert isinstance(config.LIVE_MODE, bool)
