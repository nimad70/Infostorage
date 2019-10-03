# Author: Nima Daryabar aka nmdr
# Keeping usernames and password
from db import connect_db
import datetime
# from collections import *


""" Get info about user's account and 
    return his username, password, comments and app name
"""
def get_info(item_count):
    print(item_count)
    account_info = []

    counter_ = 0
    while counter_ != item_count:
        print("\nEnter info num.", counter_+1)
        # Get info from user about his account
        app_name = input("\nEnter website or application's name: ")
        username_ = input("Enter username: ")
        password_ = input("Enter password: ")
        comments = ""

        # Check if user enter correct answer to y/n question about comments
        comments_check_answer = True
        while comments_check_answer:
            
            # Check if user has any comments about his info
            is_comments = input("Have any comments(y/n)? ")

            # Yes
            if is_comments == 'y':
                comments = input("Enter Your comments:  ")
                comments_check_answer = False
                break
            
            # No
            elif is_comments == 'n':
                print("Good!")
                comments_check_answer = False
                break
            
            # Wrong answer
            else:
                print("\nWrong answer to y/n! Enter again plz.")
        
        account_info.append((app_name, username_, password_, comments))
        counter_ += 1

    return account_info


# Validating user's account info
def validate_info(web_name, user_name, pass_word, comments):
    # validate username, ... by their sizes and other things
    # return validated data
    pass

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
        count = int(input("How many items do you want to enter: "))
        info_list = get_info(count)
        print(info_list)

        





        # move above code to get_info() func
        # impor_func(validated_data)





        check_retrieve_import = False
        pass
    
    # Wrong answer to retrieve(r) or import(i)
    else:
        print("\n*Wrong answer, Enter again plz!")