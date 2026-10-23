from src.transform import validate_weather

def test_validate_weather():
    weather = {
        "current":{
            "time": "2026-10-23T08:00",
            "temperature_2m":25.0,
            "relative_humidity_2m":40
        }
    }

    result  = validate_weather(weather)

    assert result["temperature_2m"] == 25.0
    assert result["relative_humidity_2m"] == 40