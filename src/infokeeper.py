# Author: Nima Daryabar aka nmdr
# Storing applications username and password
from db import connect_db
import datetime
from account import get_info
from db_collections import make_collection
from regcheck import digit_check


# connect to database or create one
db, new_database = connect_db()
print("\n", db, "\n", new_database)

#  continue retrieving or importing data to database or end the program
check_to_continue_retrieve_import = True
while check_to_continue_retrieve_import:

    # Check to enter the correct letter for retrieving or importing data
    while True:

        # Asking about retrieving or importing data or end
        answer_retrieve_import_end = input("\nRetrieve(r) or"
            " Import(i) data from/into the database or end(e)\n[r/i/e]: ")

        if answer_retrieve_import_end == 'r': # Retrieving data from database
            # if user has just created a new database
            if new_database:
                print("\n -> You've just created a new database, "
                    "first you should import some data into it!")
            # If there is data in database
            else:
                print(answer_retrieve_import_end)
                # retrieve_data(db)
                break

        elif answer_retrieve_import_end == 'i': # Import data into database
            print(answer_retrieve_import_end)
            
            # Get number of items they want to import into the database
            print("\nHow many items do you want to enter:", end=' ')
            # Check only digits are entered
            count = digit_check()
            
            info_list = get_info(count)
            print(info_list)

            #  Ask if user is sure about to import data into the choosen database
            check_to_import = True
            while check_to_import:
                answer_to_import = input("\nare you sure you want to import data to database(y/n)? ")
                if answer_to_import == 'y':
                    print("okay")

                    # -----------------------------------------------------------
                    # insert data into database
                    # ins_result = insert_data(db, info_list, count)
                    make_collection(db, info_list, count)
                    # -----------------------------------------------------------
                    
                    check_to_import = False
                elif answer_to_import == 'n':
                    print("Good!")
                    check_to_import = False
                else:
                    print("*Wrong answer, Try again!")
            break
        
        elif answer_retrieve_import_end == 'e': # End retrieving or importing
            break

        else: # Wrong answer to retrieve(r) or import(i)
            print("\n*Wrong answer, Enter again plz!")

    # Check to keep retrieving or importing data or end program
    while True:
        check_answer = input("\n> start retrieving or importing data again (y/n)? ")
        if check_answer == 'n': # Stop program
            check_to_continue_retrieve_import = False
            break
        elif check_answer == 'y': # Continue
            break
        else: # Wrong answer
            print("*Wrong answer, Enter again please!")