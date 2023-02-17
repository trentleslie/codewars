--# Given a demographics table in the following format:

--# ** demographics table schema **

--# id
--# name
--# birthday
--# race
--# you need to return a table that shows a count of each race represented, ordered by the count in descending order as:

--# ** output table schema **

--# race
--# count

--# chatgpt got this on the first try, then again, I probably could have too
SELECT 
  race, 
  COUNT(*) AS count
FROM 
  demographics 
GROUP BY 
  race 
ORDER BY 
  count DESC;

--# top codewars solution

SELECT race, COUNT(race)
FROM demographics
GROUP BY race
ORDER BY Count(race) desc
