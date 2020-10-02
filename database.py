import psycopg2
import psycopg2.extras


# for all functions except find_Hero_OneDay, I did injection protection by ignore inputs
# that contain semicolon or single-quote.
# for find_Hero_OneDay function, the inputs should be all integer, I did injection protection
# in application.py.

class All_functions:
    def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string)
    
    def find_Department(self,state):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(
            "SELECT * FROM directory"
        )
        record = cursor.fetchall()
        return record

    def find_Department2(self,city):
        if ';' in city:
            print('\n######################################################################')
            print('## Warning: Limited user rights. You should follow the instruction! ##')
            print('######################################################################\n')
            return
        if '\'' in city:
            print('\n######################################################################')
            print('## Warning: Limited user rights. You should follow the instruction! ##')
            print('######################################################################\n')
            return
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(
            "SELECT department_name, address, phone FROM directory left join zip_table on directory.zip = zip_table.zip where city = UPPER(%s)", (city,)
        )
        record = cursor.fetchall()
        return record
    
    
    def find_Hero_inCity(self,city):
        if ';' in city:
            print('\n######################################################################')
            print('## Warning: Limited user rights. You should follow the instruction! ##')
            print('######################################################################\n')
            return
        if '\'' in city:
            print('\n######################################################################')
            print('## Warning: Limited user rights. You should follow the instruction! ##')
            print('######################################################################\n')
            return
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(
            "select fname, frank, department, location from (firefighters left join directory on firefighters.department = directory.department_name)as temp1 left join zip_table on temp1.zip = zip_table.zip where city = UPPER(%s)", (city,)
        )
        record = cursor.fetchall()
        return record
    
    
    
    def find_Hero_OneDay(self,month, day):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if month == 0:
            cursor.execute(
                "select * from firefighters where date_part('month', NOW()) = date_part('month', deathdate) AND date_part('day', NOW()) = date_part('day', deathdate)"
            )
        else:
            
            cursor.execute(
                "select * from firefighters where %s = date_part('month', deathdate) AND %s = date_part('day', deathdate)", (month,day,)
            )            
        
        record = cursor.fetchall()
        return record     
    
    def find_Population(self,location, year):
        if ';' in location:
            print('\n######################################################################')
            print('## Warning: Limited user rights. You should follow the instruction! ##')
            print('######################################################################\n')
            return
        if '\'' in location:
            print('\n######################################################################')
            print('## Warning: Limited user rights. You should follow the instruction! ##')
            print('######################################################################\n')
            return
        if ';' in year:
            print('\n######################################################################')
            print('## Warning: Limited user rights. You should follow the instruction! ##')
            print('######################################################################\n')
            return
        if '\'' in year:
            print('\n######################################################################')
            print('## Warning: Limited user rights. You should follow the instruction! ##')
            print('######################################################################\n')
            return
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(
            "select geo, year, program, population from population where year = %s and geo = initcap(%s)", (year,location,)
        )
        record = cursor.fetchall()
        return record
    
    
    def find_Volunteer(self,county, year):
        if ';' in county:
            print('\n######################################################################')
            print('## Warning: Limited user rights. You should follow the instruction! ##')
            print('######################################################################\n')
            return
        if '\'' in county:
            print('\n######################################################################')
            print('## Warning: Limited user rights. You should follow the instruction! ##')
            print('######################################################################\n')
            return
        if ';' in year:
            print('\n######################################################################')
            print('## Warning: Limited user rights. You should follow the instruction! ##')
            print('######################################################################\n')
            return
        if '\'' in year:
            print('\n######################################################################')
            print('## Warning: Limited user rights. You should follow the instruction! ##')
            print('######################################################################\n')
            return
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(
            "select year,county,name, requested, spent, grant_amount from volunteer where year = %s and county = UPPER(%s)", (year,county,)
        )
        record = cursor.fetchall()
        return record    
    
    
    
    
    
    
    