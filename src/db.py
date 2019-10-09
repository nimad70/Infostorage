# Author: Nima Daryabar
# Making a database using pymongo
from pymongo import MongoClient
import re


#  you are in db_dev .. do some changes in here
#  regex : ^([a-zA-Z]+)$






# Connecting to the database
def connect_db():
    # Running Mongod instance
    client = MongoClient('localhost', 27017)

    database_list = db_list(client)

    # Asking user to make a new db or used one from the list
    new_db = False
    check_answer_to_make_new_db = True
    while check_answer_to_make_new_db:
        answer_new_or_list = input("\nMaking new datbase(n) or Using one from list(l) - (n/l): ")
        
        # Making a new databse
        if answer_new_or_list == 'n':

            # Check if name exists or not
            db_name_exists = True
            while(db_name_exists):
                # Getting database name from user
                db_name_user = input('\nGive a database name to create one: ')
                print(db_name_user)

                # if db name exists
                if db_name_user in database_list:
                    print("\n-> The database is already created! Enter New name plz!")
                else:
                    # Create database
                    # db = client['reg_info_db']
                    db = client[db_name_user]
                    print("\nDatabase is created")
                    db_name_exists = False
                    new_db = True
                    check_answer_to_make_new_db = False
                    break
            
        
        # Using db from old databases in the list
        elif answer_new_or_list == 'l':
            print(answer_new_or_list)
            
            # Check if user enters correct number
            check_given_number = True
            while check_given_number:
                # Getting number from user
                db_list_num = int(input("\nEnter database list number: "))
                # Check if number is in the range of db_list length
                if db_list_num in range((len(database_list)+1)):
                    check_given_number = False
                    break
                else:
                    print("Wrong number! plz enter number in a range of 1 to ", len(database_list))
            
            print(database_list[(db_list_num-1)])
            choosen_db = database_list[(db_list_num-1)]
            print("choosen:", choosen_db)
            db = client[choosen_db]
            check_answer_to_make_new_db = False
            break

        # Wrong answer to make db or use from the list question
        else:
            print("\n*Wrong answer, Enter again plz!")
        
    return db, new_db


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

"""
def create_db():
    pass



def retrieve_db():
    pass
"""


if __name__ == "__main__":
    conn = connect_db()