# Author: Nima Daryabar
# Making a database using pymongo
from pymongo import MongoClient
import re
from regcheck import *


# Show databases list
# db_client: client from connect_db()
# db_list: list of databases as return value
def db_list(db_client):
    print("\ndatabases list:\n")
    db_list = db_client.list_database_names() # Get list of databases

    # Check if collection list is empty or not to show it to the user
    if not db_list: # if no database
        print("\n-> There is no database to show!")
    else:
        for counter, dbname in enumerate(db_list, 1):
            print(counter, '.', dbname)
    return db_list


# Create new datbase
# dbls_list: database list from connect_db()
# dbls_client: client from connect_db()
def create_db(dbls_list, dbls_client):
    is_new_db = True # True if new db is created
    while True: # Check if name exists or not

        # Getting database name from user
        while True: # Check if name is only letters
            db_name_user = input('\nGive a database name to create one: ')

            # check if name is only letters
            if check_only_letters(db_name_user): # if True
                break
            else:
                print("\n -> only letters is allowed")

        
        if db_name_user in dbls_list: # if database name is in the list
            print("\n-> The database is already created! Enter New name plz!")

        else: # if database name is not in the list
            created_db = dbls_client[db_name_user] # Create database
            print("\nDatabase is created")
            break 
    return created_db, is_new_db


# Choose one database from databases list
# rdb_db_list: database list from connect_db()
# rdb_client: client from connect_db()
def retrieve_db(rdb_client, rdb_db_list):
    while True: # Check if user enters correct number

        # Check and get user's given number
        print("\nEnter database list number:", end=' ')
        db_list_num = digit_check()
        
        # Check if number is in the range of db_list length
        if db_list_num == 0:
            print("Wrong number! again plz!")
            continue
        if db_list_num in range((len(rdb_db_list)+1)): # if number is in the range
            break # break from loop
        else:
            print("Wrong number! plz enter a number in a range of 1 to ", len(rdb_db_list))
    
    print(rdb_db_list[(db_list_num-1)]) # show choosen database from list
    choosen_db = rdb_db_list[(db_list_num-1)] # choose from database list
    retrieved_db = rdb_client[choosen_db] # return and store choosen database 
    return retrieved_db


# Connecting to the database
def connect_db():
    client = MongoClient('localhost', 27017) # Running Mongod instance
    database_list = db_list(client) # Show databases list

    # Turn to True if user makes a new database
    new_db = False

    # Check if there is any db in db_list to make a new database or not
    if not database_list: # if no database in database list
        print("\nCreate a database to continue")
        db, new_db = create_db(database_list, client) # Create a new database

    else: # if there is db in database list
        while True: # Ask to make a new database or use one from the list
            answer_new_or_list = input("\nMaking new datbase(n) or Using one from list(l) - (n/l): ")
            
            if answer_new_or_list == 'n': # Making a new databse
                db, new_db = create_db(database_list, client) # Create new database
                break
                
            elif answer_new_or_list == 'l': # Using db from old databases in the list
                db = retrieve_db(client, database_list) # Choose one from db list
                break

            
            else: # Wrong answer to the question
                print("\n*Wrong answer, Enter again plz!")
    return db, new_db


if __name__ == "__main__":
    conn = connect_db()
