CREATE USER [username] WITH PASSWORD [password];
GRANT ALL PRIVILEGES ON DATABASE firedepartment TO [username];
GRANT ALL PRIVILEGES ON TABLE firefighters TO [username];
GRANT ALL PRIVILEGES ON TABLE directory TO [username];
GRANT ALL PRIVILEGES ON TABLE volunteer TO [username];
GRANT ALL PRIVILEGES ON TABLE population TO [username];
GRANT ALL PRIVILEGES ON TABLE zip_table TO [username];
SET client_encoding TO 'WIN1252';
