CREATE TABLE IF NOT EXISTS  volunteer
(
    year int,
    county varchar(100),
    name  varchar(150),
    code  varchar(150),
    requested double precision,
    spent double precision,
    grant_amount double precision,
    PRIMARY KEY(year,code)
);
