import csv

def setup(conn):
    # all csv files name
    f_csv = "New_York_State_Fallen_Firefighters_Memorial_Roll_of_Honor.csv"
    d_csv = "Fire_Department_Directory_for_New_York_State.csv"    
    v_csv = "Volunteer_Fire_Assistance_Grants_Awarded__Beginning_2009.csv"
    p_csv = "Annual_Population_Estimates_for_New_York_State_and_Counties__Beginning_1970.csv"
    z_csv = "zipTable.csv"
    # create schemas
    with conn.cursor() as cursor:
        setup_queries = open('firefighters.sql', 'r').read()
        cursor.execute(setup_queries)
        setup_queries = open('directory.sql', 'r').read()
        cursor.execute(setup_queries)
        setup_queries = open('volunteer.sql', 'r').read()
        cursor.execute(setup_queries)
        setup_queries = open('population.sql', 'r').read()
        cursor.execute(setup_queries)
        setup_queries = open('zipTable.sql', 'r').read()
        cursor.execute(setup_queries)
        conn.commit()
    # load data into each schema
    with open(f_csv,newline='\n') as csvfile:
        red = csv.reader(csvfile)
        with conn.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE firefighters")
            for row in red:
                cursor.execute('INSERT INTO firefighters(fname,frank,department,deathdate,location) \
                               VALUES(%s,%s,%s,%s,%s)',row)
            conn.commit()
    with open(d_csv,newline='\n') as csvfile:
        red = csv.reader(csvfile)
        with conn.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE directory")
            for row in red:
                cursor.execute('INSERT INTO directory(department_name,department_code,address,zip,\
                                                      county_code,county_name,phone,latitude,longitude) \
                               VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)
            conn.commit()
    with open(v_csv,newline='\n') as csvfile:
        red = csv.reader(csvfile)
        with conn.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE volunteer")
            for row in red:
                cursor.execute('INSERT INTO volunteer(year,county,name,code,requested,spent,grant_amount) \
                               VALUES(%s,%s,%s,%s,%s,%s,%s)',row)
            conn.commit()
    with open(p_csv,newline='\n') as csvfile:
        red = csv.reader(csvfile)
        with conn.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE population")
            for row in red:
                cursor.execute('INSERT INTO population(fips,geo,year,program,population) VALUES(%s,%s,%s,%s,%s)',row)
            conn.commit()
    with open(z_csv,newline='\n') as csvfile:
        red = csv.reader(csvfile)
        with conn.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE zip_table")
            for row in red:
                cursor.execute('INSERT INTO zip_table(zip,city,state) VALUES(%s,%s,%s)',row)
            conn.commit()