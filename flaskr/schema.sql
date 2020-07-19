CREATE TABLE activity (
       id SERIAL PRIMARY KEY,
       name TEXT
);

CREATE TABLE person (
       id TEXT PRIMARY KEY,
       email TEXT
);

CREATE TABLE enrollment (
       key STRING PRIMARY KEY,
       activity INTEGER,
       person TEXT
);
