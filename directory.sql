CREATE TABLE IF NOT EXISTS directory (   
    department_name varchar(255),   
    department_code int PRIMARY KEY,    
    address varchar(255),   
    zip int,    
    county_code smallint,   
    county_name varchar(255),   
    phone varchar(255), 
    latitude double precision,  
    longitude double precision 
);  

