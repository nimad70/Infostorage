# Author: Nima Daryabar
# Making a database using pymongo
from pymongo import MongoClient
import re
from regcheck import *


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
# dbls_list: database list from connect_db()
# dbls_client: client from connect_db()
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

            # check if name is only letters
            if check_only_letters(db_name_user):
                checking_db_name = False
            else:
                print("\n -> only letters is allowed")

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


# Choose one database from databases list
# rdb_db_list: database list from connect_db()
# rdb_client: client from connect_db()
def retrieve_db(rdb_client, rdb_db_list):
    # Check if user enters correct number
    check_given_number = True
    while check_given_number:

        # Check and get user's given number
        print("\nEnter database list number:", end=' ')
        db_list_num = digit_check()
        
        # Check if number is in the range of db_list length
        if db_list_num == 0:
            print("Wrong number! again plz!")
            continue
        if db_list_num in range((len(rdb_db_list)+1)):
            check_given_number = False
            break
        else:
            print("Wrong number! plz enter a number in a range of 1 to ", len(rdb_db_list))
    
    print(rdb_db_list[(db_list_num-1)])
    choosen_db = rdb_db_list[(db_list_num-1)]
    retrieved_db = rdb_client[choosen_db]

    return retrieved_db


# Connecting to the database
def connect_db():
    # Running Mongod instance
    client = MongoClient('localhost', 27017)

    # Show databases list
    database_list = db_list(client)

    # Turn to True if user makes a new database
    new_db = False

    # Check if there is any db in db_list to make a new database or not
    if not database_list:
        print("\nCreate a database to continue")
        # Create a new database
        db, new_db = create_db(database_list, client)
    else:
        # Ask user if they want to make a new db or use one from db
        check_answer_to_make_new_db = True
        while check_answer_to_make_new_db:
            answer_new_or_list = input("\nMaking new datbase(n) or Using one from list(l) - (n/l): ")
            
            # Making a new databse
            if answer_new_or_list == 'n':
                # Create new database
                db, new_db = create_db(database_list, client)
                check_answer_to_make_new_db = False
                break
                
            # Using db from old databases in the list
            elif answer_new_or_list == 'l':
                # Choose one from db list
                db = retrieve_db(client, database_list)
                check_answer_to_make_new_db = False
                break

            # Wrong answer to make db or use from the list question
            else:
                print("\n*Wrong answer, Enter again plz!")
        
    return db, new_db


if __name__ == "__main__":
    conn = connect_db()