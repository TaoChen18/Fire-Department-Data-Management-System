CREATE TABLE IF NOT EXISTS firefighters   
(   
    fname  varchar(255),   
    frank  varchar(255),   
    department  varchar(255),   
    deathdate date,   
    location  varchar(255), 
    PRIMARY KEY(fname,department,deathdate)
);
