SELECT 
observation_time,
temperature,
humidity
FROM weather_observations
ORDER BY observation_time DESC;

SELECT ROUND(AVG(temperature)::numeric,2) AS  average_temperature
FROM weather_observations; 

SELECT MAX(temperature) AS hottest_temperature
FROM weather_observations;

SELECT ROUND(AVG(humidity)::numeric,2) AS average_humidity
FROM weather_observations;