CREATE TABLE IF NOT EXISTS weather_observations(
id SERIAL PRIMARY KEY,
observation_time TIMESTAMP NOT NULL,
temperature REAL NOT NULL,
humidity INTEGER NOT NULL
);