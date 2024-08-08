# Write your MySQL query statement below
-- SELECT name from Customer where referee_id <> 2 or referee_id is null;
-- SELECT name from Customer where referee_id != 2 is not false ;
SELECT name FROM Customer WHERE COALESCE(referee_id,1) <> 2;
