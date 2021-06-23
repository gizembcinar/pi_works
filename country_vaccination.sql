select country_vaccination.country, country_vaccination.date, 
       CASE WHEN country_vaccination.daily_vaccinations IS NULL THEN 
            (CASE WHEN med_t.median_vac IS NULL THEN 0 ELSE med_t.median_vac END) 
       ELSE country_vaccination.daily_vaccinations
       END ,
       country_vaccination.vaccines
from country_vaccination
left join (SELECT country, PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER BY daily_vaccinations) median_vac
       FROM country_vaccination
       GROUP BY country) med_t
on med_t.country = country_vaccination.country;

