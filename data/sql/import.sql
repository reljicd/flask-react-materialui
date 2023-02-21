COPY countries(country, code, population, gdp)
FROM '/raw-data/dictionary.csv'
DELIMITER ','
CSV HEADER;

COPY medals(year, city, sport, discipline, athlete, country_code, gender, event, medal)
FROM '/raw-data/2004-2012.csv'
DELIMITER ','
CSV HEADER;