-- Hive Script Example for creation of an SQL table that stores the data of a file users.csv
-- This script creates a table and inserts data into it.

-- Create table
CREATE TABLE IF NOT EXISTS users (
    name STRING,
    age INT
);

-- Load data into table
LOAD DATA INPATH 'users.csv' OVERWRITE INTO TABLE users;

-- Query the table
SELECT name, age FROM users WHERE age > 25;
