# Author: Nima Daryabar aka nmdr
# Storing applications username and password
import datetime

from src.accounts.account import get_info
from src.database.db import connect_db
from src.database.db_collections import make_collection
from src.database.db_collections import retrieve_data
from src.validation.regcheck import digit_check


# connect to database or create one
db, new_database = connect_db()

#  continue retrieving or importing data to database or end the program
check_to_continue_retrieve_import = True
while check_to_continue_retrieve_import:

    # Check to enter the correct letter for retrieving or importing data
    while True:
        # Asking about retrieving or importing data or end
        answer_retrieve_import_end = input(
            "\n1. Retrieve data from database: r"
            "\n2. Import data into database: i"
            "\n3. End: e"
            "\n\n[r/i/e]: ")

        if answer_retrieve_import_end == 'r': # Retrieving data from database
            if new_database: # if user has just created a new database
                print("\n -> You've just created a new database, "
                    "first you should import some data into it!")
            else: # If there is data in database
                retrieve_data(db) # Retrieve data from database
                break

        elif answer_retrieve_import_end == 'i': # Import data into database
            # Get number of items they want to import into the database
            print("\nHow many items do you want to enter:", end=' ')
            count = digit_check() # Check only digits are entered            
            info_list = get_info(count) # Get user account information
            while True: # Ask if user is sure about to import data into database
                answer_to_import = input("\nare you sure you want to import data to database(y/n)? ")
                if answer_to_import == 'y':
                    make_collection(db, info_list, count)
                    break
                elif answer_to_import == 'n':
                    break
                else: # Wrong answer to the question
                    print("*Wrong answer, Try again!")
        
        elif answer_retrieve_import_end == 'e': # End retrieving or importing
            break

        else: # Wrong answer to retrieve(r) or import(i)
            print("\n*Wrong answer, Enter again plz!")

    while True: # Check to keep retrieving or importing data or end program
        check_answer = input("\n> start retrieving or importing data again (y/n)? ")
        if check_answer == 'n': # Stop program
            check_to_continue_retrieve_import = False
            break
        elif check_answer == 'y': # Continue
            break
        else: # Wrong answer
            print("*Wrong answer, Enter again please!")
