--# For this challenge you need to create a simple query to display each unique clan with their total points and ranked by their total points.

--# people table schema
--# name
--# points
--# clan
--# You should then return a table that resembles below

--# select on
--# rank
--# clan
--# total_points
--# total_people
--# The query must rank each clan by their total_points, you must return each unqiue clan and if there is no clan name (i.e. it's an empty string) you must replace it with [no clan specified], you must sum the total_points for each clan and the total_people within that clan.


# using chatgpt, it failed at first by trying to call total_points before it was defined, so I had to move the order by clause to the end
SELECT 
  ROW_NUMBER() OVER (ORDER BY SUM(points) DESC) AS rank,
  COALESCE(NULLIF(clan, ''), '[no clan specified]') AS clan,
  SUM(points) AS total_points,
  COUNT(*) AS total_people
FROM people
GROUP BY clan
ORDER BY SUM(points) DESC

--# top codewars solution

SELECT RANK() OVER (ORDER BY SUM(points) DESC),
  COALESCE(NULLIF(clan,''), '[no clan specified]') AS clan,
  SUM(points) AS total_points,
  COUNT(*) AS total_people
FROM people 
GROUP BY clan
ORDER BY total_points DESC