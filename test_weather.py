from weather import get_alerts, get_forecast

def test_tools_exist():
    """Simple test to verify tool functions are defined."""
    assert get_alerts is not None
    assert get_forecast is not None
