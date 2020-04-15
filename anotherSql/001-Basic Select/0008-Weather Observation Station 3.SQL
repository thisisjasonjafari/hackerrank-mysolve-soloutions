--  Query a list of CITY and STATE from the STATION table.

-- Input Format

-- The STATION table is described as follows:
 
SELECT DISTINCT (CITY)   FROM STATION   WHERE MOD(ID , 2) = 0;  