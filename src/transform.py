
def validate_weather(weather):
    if "current" not in weather:
        raise ValueError("Missing current weather data")

    current = weather["current"]

    if "temperature_2m" not in current:
        raise ValueError("Missing temperature")

    if "relative_humidity_2m" not in current:
        raise ValueError("Missing humidity")

    if not isinstance(current["temperature_2m"],(int,float)):
        raise ValueError("Temperature must be a number")

    if not isinstance(current["relative_humidity_2m"],(int, float)):
        raise ValueError("Humidity must be a number")

    return current

if __name__ == "__main__":
    from ingest import fetch_weather

    weather =   fetch_weather()
    current = validate_weather(weather)

    print("Weather data validated successfully!")
    print(current)
