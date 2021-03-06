# Schema description:

We divide 'Fire_Department_Directory_for_New_York_State.csv' table into two part: 'Fire_Department_Directory_for_New_York_State.csv' and
'zipTable.csv'. Because 'zipcode' decides the 'city' and 'state'. We could have got another table to focus on 'county code' and 'county name',
but we didn't do that. The reason is that 'county code' together with 'state' decides 'county name' and county name is used only in this
'Fire_Department_Directory_for_New_York_State.csv' table. So we think to build another table focusing on 'county code' and 'county name' helps
nothing but make it more complicated.

# Data type description:
```postgresql
	CREATE TABLE IF NOT EXISTS directory (   
	    department_name varchar(255),			-- [long string formed with multiple words. eg: SOUTHPORT FIRE DEPARTMENT]   
	    department_code int PRIMARY KEY,    	-- [4 or 5 digit number. eg: 54013]   [***department code decides all ohter column]
	    address varchar(255),   
	    zip int,    							-- [5 digit number. eg: 14895]       
	    county_code smallint,					-- [1 or 2 digit number. eg: 19]    
	    county_name varchar(255),   
	    phone varchar(255), 					-- [10 digit number. eg: 5856699342]   
	    latitude double precision,  			-- [decimal number. eg: 43.18617]   
	    longitude double precision   			-- [decimal number. eg: -77.80389]   
	);  

	CREATE TABLE IF NOT EXISTS zip_table		
	(		
	    zip int PRIMARY KEY,    				-- [5 digit number. eg: 14895]      [***zipcode decides all ohter column]     		
	    city varchar(255),		
	    state char(5)    						-- [2 character string. eg: NY]       	
	);		

	CREATE TABLE IF NOT EXISTS firefighters   
	(   
	    fname  varchar(255),   
	    frank  varchar(255),   					-- [single word string. eg: captain] 		   
	    department  varchar(255),   
	    deathdate date,							-- [date. eg: 2001/9/11] 	  
	    location  varchar(255),
	    PRIMARY KEY(fname,department,deathdate) -- [***assume that no two people in the same department died in the same day. data shows the same thing]  
	);

	CREATE TABLE IF NOT EXISTS population			
	(			
	  fips int,									-- [5 digit number. eg: 36000]   
	  geo varchar(100),   						-- [single word string. eg: Hamilton] 			
	  year int,									-- [4 digit number. eg: 2010]   			
	  program   varchar(100),					-- [multiple words string. eg: Postcensal Population Estimate] 		
	  population int,			
	  PRIMARY KEY(fips,year)					-- [***fips is code for county name. same county with same year decides all other column]  
	);

	CREATE TABLE IF NOT EXISTS volunteer
	(
	    year int,								-- [4 digit number. eg: 2010]   
	    county varchar(100),   					-- [single word string. eg: COLUMBIA] 		
	    name  varchar(150),						-- [multiple words string. eg: GREENPORT FIRE DISTRICT] 	
	    code  varchar(150),						-- [5 digit number. eg: 42013]   
	    requested double precision,   			-- [decimal number. eg: 3257.61]
	    spent double precision,   				-- [decimal number. eg: 2191.25]
	    grant_amount double precision,   		-- [decimal number. eg: 470.96]
	    PRIMARY KEY(year,code)					-- [***same county code with same year decides all other column]  
	);
```

# Running guidance:

1. To run our system, you should install psycopy2 in python and in Command Prompt. There is related guidance online.

2. Create Database "firedepartment" in super user "postgres" using postgresql.
		- Open Command Prompt
		- enter "psql -U postgres"
		- enter your password
		- Type "CREATE DATABASE firedepartment"

3. In the 'main_file.txt' file, we store Postgres user name and password. You should change it into your own user name and password.

4. To run the firedepartment application
		- In Command Prompt, change the directory to where the 'application.py' file locates
		- Run the command line 'python application.py'

5. You should register when you first use this system. Your user name and password are not allowed to contain a special character.
   You can not register if the user name exists already.
		- press 2 to create user name and password.
		- type in your user name and password. When it succeeds, the interface will go back to the first scene.
		- press 1 to log in with your user name and password.
