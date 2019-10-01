# Author: Nima Daryabar aka nmdr
# Keeping usernames and password
from db import connect_db
import datetime
# from collections import *


# connect to database or create one
"""
db, new_database = connect_db()
print("\n", db, "\n", new_database)
"""

# Check if user enters the correct letter for retrieving or importing data from/into database
check_retrieve_import = True
while check_retrieve_import:
    answer_retrieve_import = input("\nRetrieve(r) data from database or"
        "Import(i) new data into the database(r/i): ")

    # Retrieving data from database
    if answer_retrieve_import == 'r':
       pass
       """
        # Check if user has just created a new database and db is empty
        if new_database:
            print("You've just created a new database, "
                "first you should import some data into database!")
        # If there is data in database
        else:
            print(answer_retrieve_import)
            # retrieve_data(db)








            check_retrieve_import = False
        """

    # Import data into database
    elif answer_retrieve_import == 'i':
        print(answer_retrieve_import)

        
        # Website or application name
        web_app_name = input("Enter website or application's name: ")
        username_ = input("Enter username: ")
        password_ = input("Enter password")



        # get username
        # get password
        # get web name
        # get user comments



        check_retrieve_import = False
        pass
    
    # Wrong answer to retrieve(r) or import(i)
    else:
        print("\n*Wrong answer, Enter again plz!")