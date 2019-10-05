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

    info_sympol = ""
    
    counter_ = 0
    while counter_ != item_count:
        print("\nEnter info num.", counter_+1)
        # Get info from user about his account

        # Website/app's name
        """ Turn is_validated from to False for every step
            cause for other info except 'app' it will still be 'True'
            and if it doesn't turn to 'False' it will not check other whiles
        """
        is_validated = False
        # Website/App's name validation
        while not is_validated:
            app_name = input("\nEnter website or application's name: ")
            info_sympol = 'app'
            if validate_info(app_name, info_sympol):
                is_validated = True
            else:
                print("Plz try again!\n")

        # User account's Username
        is_validated = False
        # Username validation
        while not is_validated:
            username_ = input("Enter username: ")
            info_sympol = 'usnm_pass'
            if validate_info(username_, info_sympol):
                is_validated = True
            else:
                print("Plz try again!\n")

        
        # User account's Password
        is_validated = False
        # Password validation
        while not is_validated:
            password_ = input("Enter password: ")
            info_sympol = 'usnm_pass'
            if validate_info(password_, info_sympol):
                is_validated = True
            else:
                print("Plz try again!\n")


        # User's comments about their info
        comments = ""

        # Check if user enter correct answer to y/n question about comments
        comments_check_answer = True
        while comments_check_answer:
            
            # Check if user has any comments about his info
            has_comments = input("Have any comments(y/n)? ")

            # Yes
            if has_comments == 'y':
                # Comment validation
                is_validated = False
                while not is_validated:
                    comments = input("Enter Your comments:  ")
                    info_sympol = 'cmnt'
                    if validate_info(comments, info_sympol):
                        is_validated = True
                    else:
                        print("Plz try again!\n")
                
                comments_check_answer = False
                break
            
            # No
            elif has_comments == 'n':
                print("Good!")
                comments_check_answer = False
                break
            
            # Wrong answer
            else:
                print("\nWrong answer to y/n! Enter again plz.")
        
        account_info.append((app_name, username_, password_, comments))
        counter_ += 1

    return account_info



""" Validating user's account info
    Getting account info as value(username or password or ...) 
    and info Symbol tp check which one is which
    and return True/False as it's validate data or not
"""
def validate_info(val, symb):
    is_valid = False

    # Checking if app/website's name is coorect
    if symb == 'app':
        print(val)
        if not(not(val and not val.isspace())):
            if (len(val) > 50):
                print("\n-> More than 50 letters!")
            else:
                is_valid = True
        else:
            print("it should not leave empty!")
    
    # username and password are the same in validation
    elif symb == 'usnm_pass':
        print(val)
        if not(not(val and not val.isspace())):
            if (len(val) > 30):
                print("More than 30 letters!")
            else:
                is_valid = True
        else:
            print("it should not leave empty!")
    
    # comments - first we should check if there is comments 
    elif symb == 'cmnt':
        print(val)
        if not(not(val and not val.isspace())):
            if (len(val) > 150):
                print("More than 150 letters!")
            else:
                is_valid = True
        else:
            print("it should not leave empty!")

    else:
        print("Wrong symbol! and that's not ypur fault!")

    return is_valid


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

        





        # move above code to get_info() func
        # impor_func(validated_data)

        # show user their info and ask them if they want to save it or not based on what they enter





        check_retrieve_import = False
        pass
    
    # Wrong answer to retrieve(r) or import(i)
    else:
        print("\n*Wrong answer, Enter again plz!")