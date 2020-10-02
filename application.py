import load_data
from database import All_functions
import psycopg2


# the format of city column in population table Start with a capital letter, everything else is lowercase
# this function is to convert user's input in function find_Population into the suitable format
def format_name(s):
    return s[0].upper() + s[1:].lower() 

# load the data into firedepartment database
print('\nInitializing, please wait......\n')
main = open('main_file.txt','r').read()
conn = psycopg2.connect(main)
load_data.setup(conn)
login = True
while login==True:
    print('\
                           Welcome to Fire Department Information System!                           \n\
                                           Version 1.1.0                                            \n\
                                Authors: Tao Chen, Xingcheng Dong                                   \n\
                                                                                                    \n\
                       ######################################################                       \n\
                       ## Attention:                                       ##                       \n\
                       ##                                                  ##                       \n\
                       ## This is just a test application, and the datasets##                       \n\
                       ## are only limited to New York State. To get other ##                       \n\
                       ## states information, please just google it!       ##                       \n\
                       ##                                                  ##                       \n\
                       ## Thank you and have a nice trip!                  ##                       \n\
                       ##                                                  ##                       \n\
                       ######################################################                       \n\
----------------------------------------------------------------------------------------------------\n\
                                                                                       \n\
 Menu:                                                                                 \n\
 1. Sign in to the system (Already has an account)                                     \n\
 2. Sign up a new account                                                              \n\
 3. Exit                                                                               \
                                                                                       ')
    option = input(' Please choose a number:')
    if option == '3':
        exit()
    if option == '2': # sign up
        signup = True
        while signup == True:
            print('\n\
----------------------------------------------------------------------------------------------------\n\
                                                                                       \n\
Fire Department Information System                                                     \n\
                                                                                       \n\
                                  Sign up to our system                                \n\
                                                                                       \n')
            newuser = input('                  Username: ')
            newpass = input('                  Password: ')
            usercreation = open('usercreation.sql','r')
            user_list = [line.rstrip('\n') for line in usercreation]
            if newuser=='' or newpass=='':
                print('\n#########################################################')
                print('## Warning: Username and password should not be empty! ##')
                print('#########################################################\n')
                continue
            # replace the [username] and [password] in usercreation.sql for creating new user
            t_list = list(user_list[0].split())
            t_list[2] = newuser
            t_list[5] = "'"+newpass+"';"
            p_list = list(user_list[1].split())
            p_list[7] = newuser+";"
            f_list = list(user_list[2].split())
            f_list[7] = newuser+";"
            d_list = list(user_list[3].split())
            d_list[7] = newuser+";"
            v_list = list(user_list[4].split())
            v_list[7] = newuser+";"
            u_list = list(user_list[5].split())
            u_list[7] = newuser+";"
            z_list = list(user_list[6].split())
            z_list[7] = newuser+";"
            # combine the splitted lines in usercreation.sql into a complete string
            def listToString(s):
                str1=" "
                return (str1.join(s))
            new_string = listToString(t_list)+listToString(p_list)+listToString(f_list)+listToString(d_list)+listToString(v_list)+listToString(u_list)+listToString(z_list)+user_list[7]
            # each sql command in usercreation.sql should be autocommitted
            conn.autocommit = True
            cursor = conn.cursor()
            try:
                # create a new user and gain him/her the privileges to do some operations for tables in firedepartment database
                cursor.execute(new_string)
                signup = False
                print('\n#######################################################################')
                print('## Congratulations! You have joined into the fire department system! ##')
                print('#######################################################################\n')            
            except:
                print('\n###########################################################################')
                print('## Warning: The user already exists in the system, please go to sign in. ##')
                print('###########################################################################\n')
                print('Operations:\n1. Retry\n2. Previous\n3. Exit')
                choose = input('Your choice: ')
                if choose == '1':
                    continue
                if choose == '2':
                    signup = False
                if choose == '3':
                    exit()
    if option == '1':  # sign in
        check = False
        while check == False:
            print('\n\
----------------------------------------------------------------------------------------------------\n\
                                                                                       \n\
Fire Department Information System                                                     \n\
                                                                                       \n\
                                  Sign in to our system                                \n\
                                                                                       \n')
            username = input('                  Username: ')
            password = input('                  Password: ')
            try:               
                # connect the user to the database
                conn_string = "host='localhost' dbname='firedepartment' user='%s' password= '%s'" % (username,password)
                conn = psycopg2.connect(conn_string)
                print('\nAuthentication success! Loading the data will take a few seconds, please wait......\n')
                function = True
                while function == True:
                    print('\n\
----------------------------------------------------------------------------------------------------\n\
\n\
 Fire Department System\n\
\n\
 Functions:\n\
\n\
 1. Test connection\n\
 2. Call Help in One City\n\
 3. Find Hero of the City\n\
 4. Find Hero of the Day\n\
 5. Find Population of One Year\n\
 6. Find Financial Status for All Departments in One County\n\
 9. Sign out')
                    service = All_functions(conn_string)
                    option = input(' Please choose a number:')
                    if option == '9': # sign out
                        login = True
                        check = True
                        break
                    if option == '1': # test connection
                        records = service.find_Department('NY')
                        print(records[0][0])
                        
                    if option == '2': # find the firedepartment information in one city
                        city = input("Enter your city name: ")
                        records = service.find_Department2(city)  #'ALBANY'  TROY  BOSTON
                        if records is None: # for injection situation
                            continue
                        print('Department Name                         Address                                 Phone Number        ')
                        print('----------------------------------------------------------------------------------------------------')
                        for line in records:
                            output = ''
                            for value in line:
                                output = output+str(value)
                                for index in range(40 - len(str(value)) ):
                                    output =output+' '
                            print(output)
    
                    if option == '3': # find hero information of a city
                        city = input("Enter your city name: ")
                        records = service.find_Hero_inCity(city)  #'ALBANY'  TROY  BOSTON
                        if records is None: # for injection situation
                            continue
                        print('Name                     Rank                     Department Name                         Location')
                        print('----------------------------------------------------------------------------------------------------')
                        for line in records:
                            output = ''
                            output = output+str(line[0]).lstrip()
                            for index in range(25 - len(str(line[0])) ):
                                output =output+' '                                    
                            output = output+str(line[1]).lstrip()
                            for index in range(25 - len(str(line[1])) ):
                                output =output+' '  
                            output = output+str(line[2]).lstrip()
                            for index in range(40 - len(str(line[2])) ):
                                output =output+' '  
                            output = output+str(line[3]).lstrip()
                            for index in range(10 - len(str(line[3])) ):
                                output =output+' '
                            print(output)
    
    
                    if option == '4': # find the anniversary for heros
                        Choose = int(input('\n1. Today\n2. One specific day\n: '))
                        if Choose == 1:
                            records = service.find_Hero_OneDay(0, 0)
                        else:
                            month = input('Enter the month: ')
                            day = input('Enter the day: ')
                            # for injection protection
                            try: # since month and day should only be integer. Other characters in input will raise errors
                                records = service.find_Hero_OneDay(month, day)
                            except:
                                print('\n######################################################################')
                                print('## Warning: Limited user rights. You should follow the instruction! ##')
                                print('######################################################################\n')
                                continue
                      
                        print('Name                     Rank                     Death Date                              Location')
                        print('----------------------------------------------------------------------------------------------------')
                        for line in records:
                            output = ''
                            output = output+str(line[0]).lstrip()
                            for index in range(25 - len(str(line[0])) ):
                                output =output+' '                                    
                            output = output+str(line[1]).lstrip()
                            for index in range(25 - len(str(line[1])) ):
                                output =output+' '  
                            output = output+str(line[3]).lstrip()
                            for index in range(40 - len(str(line[3])) ):
                                output =output+' '  
                            output = output+str(line[4]).lstrip()
                            for index in range(10 - len(str(line[4])) ):
                                output =output+' '
                            print(output)
    
      
    
                    if option == '5': # find population situation of a city
    
                        location = input('Enter the location: ')
                        year = input('Enter the year: ')
                        records = service.find_Population(format_name(location), year)
                        if records is None: # for injection situation
                            continue
                        print('City                     Year                     Program                                 Population')
                        print('----------------------------------------------------------------------------------------------------')
                        for line in records:
                            output = ''
                            output = output+str(line[0]).lstrip()
                            for index in range(25 - len(str(line[0])) ):
                                output =output+' '                                    
                            output = output+str(line[1]).lstrip()
                            for index in range(25 - len(str(line[1])) ):
                                output =output+' '  
                            output = output+str(line[2]).lstrip()
                            for index in range(40 - len(str(line[2])) ):
                                output =output+' '  
                            output = output+str(line[3]).lstrip()
                            for index in range(10 - len(str(line[3])) ):
                                output =output+' '
                            print(output)    
                            
                            
                    if option == '6': # find financial situation of all firedepartmens in a city
    
                        county = input('Enter the county: ')
                        year = input('Enter the year: ')
                        records = service.find_Volunteer(county, year)
                        if records is None: # for injection situation
                            continue
                        print('Year        County      Department                              Request     Spent       Grant')
                        print('----------------------------------------------------------------------------------------------------')
                        for line in records:
                            output = ''
                            output = output+str(line[0]).lstrip()
                            for index in range(12 - len(str(line[0])) ):
                                output =output+' '                                    
                            output = output+str(line[1]).lstrip()
                            for index in range(12 - len(str(line[1])) ):
                                output =output+' '  
                            output = output+str(line[2]).lstrip()
                            for index in range(40 - len(str(line[2])) ):
                                output =output+' '  
                            output = output+str(line[3]).lstrip()
                            for index in range(12 - len(str(line[3])) ):
                                output =output+' '
                            output = output+str(line[4]).lstrip()
                            for index in range(12 - len(str(line[4])) ):
                                output =output+' '                        
                            output = output+str(line[5]).lstrip()
                            for index in range(12 - len(str(line[5])) ):
                                output =output+' '                        
                            print(output)       
            except:
                print('\n###################################################')
                print('## Warning: The username or password is invalid! ##')
                print('###################################################\n')
                print('Operations:\n1. Retry\n2. Previous\n3. Exit')
                choose = input('Your choice: ')
                if choose == '1':
                    continue
                if choose == '2':
                    login = True
                    break
                if choose == '3':
                    exit()                          
                 
       
