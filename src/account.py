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
        print("\nEnter account info number.{}:".format(counter_+1))

        # Get website/app name
        while True:
            app_name = input("\nEnter website or application name: ")
            # Website/App name validation
            if appname_validation(app_name):
                break
            else:
                print("try again!\n")

        # Get Username
        while True:
            username_ = input("\nEnter username: ")
            # Username validation
            if username_validation(username_):
                break
            else:
                print("try again!\n")
        
        # Get Password
        while True:
            password_ = input("\nEnter password: ")
            # Password validation
            if password_validation(password_):
                break
            else:
                print("try again!\n")


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


# Website/app name Validation
# Return True if name is valid
def appname_validation(app_val):
    is_app_valid = False
    print(app_val)
    
    # Check if name is left empty or user enters space instead of characters
    if not(not(app_val and not app_val.isspace())):

        # Check if name lenght is more than 50 letters
        if (len(app_val) > 50):
            print("-> More than 50 letters,", end=' ')
        else:
            is_app_valid = True
    else:
        print("-> it should not leave empty,", end=' ')
    
    return is_app_valid


# Username Validation
# Return True if username is valid
def username_validation(usn_val):
    is_usn_valid = False
    print(usn_val)
    
    # Check if username is left empty or user enters space instead of characters
    if not(not(usn_val and not usn_val.isspace())):

        # Check if username lenght is more than 30 letters
        if (len(usn_val) > 30):
            print("-> More than 30 letters,", end=' ')
        else:
            is_usn_valid = True
    else:
        print("-> it should not leave empty,", end=' ')
    
    return is_usn_valid


# Password Validation
# Return True if Password is valid
def password_validation(pass_val):
    is_pass_valid = False
    print(pass_val)
    
    # Check if username is left empty or user enters space instead of characters
    if not(not(pass_val and not pass_val.isspace())):

        # Check if username lenght is more than 30 letters
        if (len(pass_val) > 30):
            print("-> More than 30 letters,", end=' ')
        else:
            is_pass_valid = True
    else:
        print("-> it should not leave empty,", end=' ')
    
    return is_pass_valid




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


if __name__ == "__main__":
    print("\nGet Info:\n")
    get_info(2)