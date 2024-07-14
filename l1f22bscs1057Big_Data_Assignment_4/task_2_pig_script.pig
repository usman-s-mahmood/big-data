-- Pig Script Example Code for demonstration with a sample table named users
-- This script calculates the average age of users from input data.

-- Load data from HDFS, the .csv file contains names and ages of users
users = LOAD 'users.csv' USING PigStorage(',') AS (name:chararray, age:int);

-- Group by and calculate average age
avg_age = FOREACH (GROUP users ALL) GENERATE AVG(users.age);

-- Store the result
STORE avg_age INTO 'avg_age_result' USING PigStorage(',');

-- Hadoop was giving installation errors on in windows, linux and even in Virtual Box. I was unable to run this code of task 2 but tried to implement the code as per documentation resource (https://cwiki.apache.org/confluence/display/Hive/)
