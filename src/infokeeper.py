# Author: Nima Daryabar aka nmdr
# Storing applications username and password
from db import connect_db
import datetime
from account import get_info, validate_info
# from collections import *



# connect to database or create one
"""
db, new_database = connect_db()
print("\n", db, "\n", new_database)
"""

# Check if user enters the correct letter for retrieving or importing data from/into database
check_retrieve_import = True
while check_retrieve_import:
    answer_retrieve_import = input("\nRetrieve(r) or"
        " Import(i) data from/into the database(r/i): ")

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
        
        # Check if user enters anything except numbers
        counter_check = True
        while counter_check:
            try:
                count = int(input("How many items do you want to enter: "))
            except ValueError:
                print("-> Wrong! Enter a number!\n")
            else:
                counter_check = False
        
        info_list = get_info(count)
        print(info_list)

        


        # show user their info and ask them if they want to save it or not based on what they enter





        check_retrieve_import = False
        pass
    
    # Wrong answer to retrieve(r) or import(i)
    else:
        print("\n*Wrong answer, Enter again plz!")