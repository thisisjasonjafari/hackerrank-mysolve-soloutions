select c.continent,floor(avg(ci.population)) as 'avg_population'
from city ci
inner join country c
ON ci.countrycode = c.code
group by c.continent;