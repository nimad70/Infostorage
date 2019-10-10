# Author: Nima Daryabar aka nmdr
# Storing applications username and password
from db import connect_db
import datetime
from account import get_info, validate_info
from db_collections import insert_data
from regcheck import digit_check



# connect to database or create one
db, new_database = connect_db()
print("\n", db, "\n", new_database)


""" Check if user wants to continue retrieving or importing data 
     _to database or end the program 
"""
check_to_continue_retrieve_import = True
while check_to_continue_retrieve_import:

    """ Check if user enters the correct letter 
         _for retrieving or importing data from/into database
    """
    check_retrieve_import = True
    while check_retrieve_import:

        # Asking about retrieving or importing data
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
            
            """ Check if user enters anything except numbers(integer) 
                 _about number of items they want to import to database"""
            print("\nHow many items do you want to enter:", end=' ')
            count = digit_check()
            
            info_list = get_info(count)
            print(info_list)
            

            """ Asking about if user is sure about data 
                 _which is going to import to the choosen database
            """
            check_to_import = True
            while check_to_import:
                answer_to_import = input("\nare you sure you want to import data to database(y/n)? ")
                if answer_to_import == 'y':
                    print("okay")

                    # insert data into database
                    # ins_result = insert_data(db, info_list, count)
                    insert_data(db, info_list, count)


                    
                    check_to_import = False
                elif answer_to_import == 'n':
                    print("Good!")
                    check_to_import = False
                else:
                    print("*Wrong answer, Try again!")

            check_retrieve_import = False
        
        # Wrong answer to retrieve(r) or import(i)
        else:
            print("\n*Wrong answer, Enter again plz!")

    # Checking about retrieving or importing data section
    check_y_n = True
    while check_y_n:
        check_answer = input("\n> start retrieving or importing data again(y/n)? ")
        if check_answer == 'n':
            check_to_continue_retrieve_import = False
            check_y_n = False
        elif check_answer == 'y':
            check_y_n = False
        else:
            print("*Wrong answer, Enter again please!")