DROP TABLE IF EXISTS us_cities;
CREATE TABLE us_cities (
    city VARCHAR(100),
    state VARCHAR(100),
    population INT,
    latitude FLOAT,
    longitude FLOAT
);
DROP TABLE IF EXISTS us_states;
CREATE TABLE us_states (
    state_code VARCHAR(2),
    state_name VARCHAR(100),
    population INT
);
