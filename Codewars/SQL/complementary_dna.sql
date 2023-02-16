
--# write your SQL statement here: you are given a table 'dnastrand' with column 'dna', return a table with column 'dna' and your result in a column named 'res'.

--# the key is to first convert to an alternative character while switching to be able to distinguish between the old and new characters, then convert back to the original character.
SELECT 
  dna,
  REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(dna, 'A', 't'),
                                                        'T', 'A'),
                                                        't', 'T'),
                                                        'C', 'g'),
                                                        'G', 'C'),
                                                        'g', 'G') AS res
FROM 
  dnastrand;

  --# top codewars solution

# well the translate function is a lot easier to use. damn that's nice.
  SELECT dna, TRANSLATE(dna, 'ATGC', 'TACG') AS res 
FROM dnastrand