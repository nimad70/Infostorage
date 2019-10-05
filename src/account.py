# Author: Nima Daryabar
# Get and validate user's account information

""" Getting user's account information and 
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

        # Website/app name
        """ Turn is_validated from to False for every step
            cause for other info except 'app' it will still be 'True'
            and if it doesn't turn to 'False' it will not check other whiles
        """
        is_validated = False
        # Website/App name validation
        while not is_validated:
            app_name = input("\nEnter website or application name: ")
            info_sympol = 'app'
            if validate_info(app_name, info_sympol):
                is_validated = True
            else:
                print("Plz try again!\n")

        # User account Username
        is_validated = False
        # Username validation
        while not is_validated:
            username_ = input("Enter username: ")
            info_sympol = 'usnm_pass'
            if validate_info(username_, info_sympol):
                is_validated = True
            else:
                print("Plz try again!\n")

        
        # User account Password
        is_validated = False
        # Password validation
        while not is_validated:
            password_ = input("Enter password: ")
            info_sympol = 'usnm_pass'
            if validate_info(password_, info_sympol):
                is_validated = True
            else:
                print("Plz try again!\n")


        # User's comments about their account information
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



# Validation section
""" Validating user's account information
    Getting account information value(username or password or ...) 
    and a symbol as an abbreviation to check which one is which
    and return True/False as it's validated data or not
"""
def validate_info(val, symb):
    is_valid = False

    # Checking if app/website name is correct
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