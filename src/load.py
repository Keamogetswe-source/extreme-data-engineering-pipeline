import psycopg
from transform import transform_weather,validate_weather
from ingest import fetch_weather



def connect_db():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="weather_db",
        user="weather_user",
        password="weather_pass"

    )

def insert_weather(conn, weather):
    query = """
INSERT INTO weather_observations
(observation_time, temperature, humidity)
VALUES (%s, %s, %s)
"""

    conn.execute(
        query,(
            weather["time"],
            weather["temperature_2m"],
            weather["relative_humidity_2m"]
        )
    )


if __name__ == "__main__":
    weather = fetch_weather()
    current = validate_weather(weather)
    cleaned = transform_weather(current)
    
    with connect_db() as conn:
        insert_weather(conn, cleaned)

    print("Weather data inserted successfully!")
    

