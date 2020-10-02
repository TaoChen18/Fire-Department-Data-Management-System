CREATE TABLE IF NOT EXISTS population			
(			
  fips int,			
  geo varchar(100),			
  year int,			
  program   varchar(100),			
  population int,
  PRIMARY KEY(fips,year)		
);			
			
			
			
