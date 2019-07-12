CREATE TABLE people (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    gender TEXT
);

CREATE TABLE cars (
    id INTEGER PRIMARY KEY,
    brand TEXT,
    model TEXT,
    power INTEGER
);

CREATE TABLE people_cars (
    person_id INTEGER,
    car_id INTEGER
);