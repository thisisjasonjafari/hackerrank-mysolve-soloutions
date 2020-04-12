SELECT
    c.company_code,
    c.founder,
    count( DISTINCT lm.lead_manager_code ),
    count( DISTINCT sm.senior_manager_code ),
    count( DISTINCT m.manager_code ),
    count( DISTINCT e.employee_code ) 
FROM
    Company c,
    Lead_Manager lm,
    Senior_Manager sm,
    Manager m,
    Employee e 
WHERE
    c.company_code = lm.company_code 
    AND lm.lead_manager_code = sm.lead_manager_code 
    AND sm.senior_manager_code = m.senior_manager_code 
    AND m.manager_code = e.manager_code 
GROUP BY
    c.company_code,
    c.founder 
ORDER BY
    c.company_code