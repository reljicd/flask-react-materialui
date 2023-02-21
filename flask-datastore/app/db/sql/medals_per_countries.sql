select countries.country,
       coalesce(n2.gold_medals, 0) as gold_medals,
       coalesce(n3.silver_medals, 0) as silver_medals,
       coalesce(n4.bronze_medals, 0) as bronze_medals,
       countries.population
from (select country_code
      from medals where country_code is not null
      group by country_code) n1
         left join (select country_code, count(country_code) as gold_medals
                    from medals
                    where medal = 'Gold'
                    group by country_code) n2
             on n1.country_code = n2.country_code
         left join (select country_code, count(country_code) as silver_medals
                          from medals
                          where medal = 'Silver'
                          group by country_code) n3
             on n1.country_code = n3.country_code
         left join (select country_code, count(country_code) as bronze_medals
                          from medals
                          where medal = 'Bronze'
                          group by country_code) n4
             on n1.country_code = n4.country_code
         join countries on n1.country_code = countries.code