-- -- -- SELECT ROUND(SUM(LAT_N) , 4) FROM STATION WHERE LAT_N > 38.7880 AND LAT_N < 137.2345;

-- -- SELECT ROUND(MAX(LAT_N) , 4) FROM STATION WHERE LAT_N < 137.2345 ;

-- SELECT ROUND(LONG_W , 4 )  FROM STATION  WHERE LAT_N = (SELECT MAX(LAT_N ) FROM  STATION WHERE LAT_N < 137.2345 ) ; 



SELECT ROUND(MIN(LAT_N) , 4) FROM STATION  WHERE LAT_N > 38.7780