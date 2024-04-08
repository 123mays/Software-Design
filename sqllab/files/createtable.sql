DROP TABLE IF EXISTS earthquakes;

CREATE TABLE earthquakes (
  time timestamp with time zone,
  latitude real,
  longitude real,
  depth real,
  mag real,
  magType text,
  rms real,
  net text,
  id text PRIMARY KEY,
  updated timestamp with time zone,
  place text,
  type text,
  depthError real,
  status text,
  locationSource text,
);


