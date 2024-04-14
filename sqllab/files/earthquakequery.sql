-- This query retrieves all earthquakes with a depth greater than 300 kilometers
SELECT id, place, depth, time
FROM earthquakes
WHERE depth > 300
ORDER BY depth DESC;

-- This query counts the number of earthquakes, grouped by their type
SELECT type, COUNT(*) AS earthquake_count
FROM earthquakes
GROUP BY type;

-- This query retrieves earthquakes located within specific latitude and longitude ranges
SELECT id, place, latitude, longitude, time
FROM earthquakes
WHERE latitude BETWEEN -40 AND 40 AND longitude BETWEEN -180 AND -70
ORDER BY time DESC;
