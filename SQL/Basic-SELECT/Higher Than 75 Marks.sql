SELECT
    Name
FROM
    `students` 
WHERE
    `Marks` > 75 
ORDER BY
    RIGHT
( NAME, 3 ),
    ID ASC;