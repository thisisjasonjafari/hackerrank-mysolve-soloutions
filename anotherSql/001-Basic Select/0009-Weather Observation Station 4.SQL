--  Query a list of CITY and STATE from the STATION table.

-- Input Format

-- The STATION table is described as follows:
 
SELECT (COUNT(  (CITY)) - COUNT(DISTINCT (CITY)) )  FROM STATION    ;  