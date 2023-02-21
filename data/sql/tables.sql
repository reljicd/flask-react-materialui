create TABLE countries (
  id SERIAL,
  country VARCHAR(50) unique,
  code VARCHAR(3) unique,
  population INTEGER,
  gdp DECIMAL,
  PRIMARY KEY (id)
);

create TABLE medals (
  id SERIAL,
  year INTEGER,
  city VARCHAR(50),
  sport VARCHAR(50),
  discipline VARCHAR(50),
  athlete VARCHAR(100),
  country_code VARCHAR(3),
  gender VARCHAR(20),
  event VARCHAR(100),
  medal VARCHAR(50),
  PRIMARY KEY (id),
  CONSTRAINT fk_country
      FOREIGN KEY(country_code)
	  REFERENCES countries(code)
);
