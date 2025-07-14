
from core.astro_scoring import score_astrological_alignment

def test_score_astrological_alignment():
    data = {'moon_phase': 'new', 'aspects': ['venus_trine_jupiter'], 'mercury_retrograde': False}
    assert score_astrological_alignment(data) == 5
