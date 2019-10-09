# Author: Nima Daryabar
# Making a database using pymongo
from pymongo import MongoClient
import re


# Show databases list
# pass 'client' from connect_db() to module as 'db_client'
# list of databases(db_list) as return value
def db_list(db_client):
    # Show all available databases
    print("\ndatabases list:\n")
    db_list = db_client.list_database_names()

    # Check if collection list is empty or not to show it to the user
    if not db_list:
        print("\n-> There is no database to show!")
    else:
        for counter, dbname in enumerate(db_list, 1):
            print(counter, '.', dbname)
    
    return db_list


# Create new datbase
def create_db(dbls_list, dbls_client):
    # Return True as a new db is created
    is_new_db = True

    # Check if name exists or not
    db_name_exists = True
    while(db_name_exists):
        # Getting database name from user
        checking_db_name = True # Check if name is only letters
        while checking_db_name:
            db_name_user = input('\nGive a database name to create one: ')
            if check_db_name(db_name_user):
                checking_db_name = False
            else:
                print("\n -> only letters is allowed")

        print(db_name_user)

        # if db name exists
        if db_name_user in dbls_list:
            print("\n-> The database is already created! Enter New name plz!")
        else:
            # Create database
            # db = client['reg_info_db']
            created_db = dbls_client[db_name_user]
            print("\nDatabase is created")
            db_name_exists = False
    
    return created_db, is_new_db


# Check db name for just letters allowed
# True False as return value
def check_db_name(db_name):
    is_db_name = True
    # only letters regex
    name_reg = re.compile('^([a-zA-Z]+)$')
    if not re.match(name_reg, db_name):
        is_db_name = False
    
    return is_db_name


# Connecting to the database
def connect_db():
    # Running Mongod instance
    client = MongoClient('localhost', 27017)

    # Show databases list
    database_list = db_list(client)

    # Turn to True if user makes a new database
    new_db = False

    # Check if there is any db in db_list to make new database or not
    if not database_list:
        print("\nCreate a database to continue")
        db, new_db = create_db(database_list, client)
    else:
        check_answer_to_make_new_db = True
        while check_answer_to_make_new_db:
            answer_new_or_list = input("\nMaking new datbase(n) or Using one from list(l) - (n/l): ")
            
            # Making a new databse
            if answer_new_or_list == 'n':
                # Create new database
                db, new_db = create_db(database_list, client)
                print(db, "\n", new_db)
                
                check_answer_to_make_new_db = False
                break
                
            # Using db from old databases in the list
            elif answer_new_or_list == 'l':
                pass
                # print(answer_new_or_list)
                
                # # Check if user enters correct number
                # check_given_number = True
                # while check_given_number:
                #     # Getting number from user
                #     db_list_num = int(input("\nEnter database list number: "))
                #     # Check if number is in the range of db_list length
                #     if db_list_num in range((len(database_list)+1)):
                #         check_given_number = False
                #         break
                #     else:
                #         print("Wrong number! plz enter number in a range of 1 to ", len(database_list))
                
                # print(database_list[(db_list_num-1)])
                # choosen_db = database_list[(db_list_num-1)]
                # print("choosen:", choosen_db)
                # db = client[choosen_db]
                # check_answer_to_make_new_db = False
                # break

            # Wrong answer to make db or use from the list question
            else:
                print("\n*Wrong answer, Enter again plz!")
        
    return db, new_db



"""
def retrieve_db():
    pass
"""


if __name__ == "__main__":
    conn = connect_db()