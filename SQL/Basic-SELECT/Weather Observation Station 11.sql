SELECT
    city
FROM
    station
WHERE
    city NOT IN (
    SELECT
    city
FROM
    station
WHERE
        LEFT ( city, 1 ) IN ( 'a', 'i', 'u', 'e', 'o' )
    AND RIGHT ( city, 1 ) IN ( 'a', 'i', 'u', 'e', 'o' ))
GROUP BY
    city