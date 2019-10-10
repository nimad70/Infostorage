# Author: Nima Daryabar
# Get and validate user's account information

""" Getting user's account information and 
    return his username, password, comments and app name
"""
def get_info(item_count):
    print(item_count)
    account_info = []

    counter_ = 0
    while counter_ != item_count:
        print("\nEnter account info number.{}:".format(counter_+1))

        # Get website/app name
        app_name = get_app_name()
        print("app name: {}".format(app_name))
        # while True:
        #     app_name = input("\nEnter website or application name: ")
        #     # Website/App name validation
        #     if appname_validation(app_name):
        #         break
        #     else:
        #         print("try again!\n")

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


        # comments about account information
        comments = ""
        # Check answer to y/n question about comments
        comments_check_answer = True
        while comments_check_answer:
            
            # Check if user has any comments about his info
            has_comments = input("Have any comments(y/n)? ")

            # Yes
            if has_comments == 'y':
                while True:
                    comments = input("\nEnter Your comments: ")
                    # Comment validation
                    if Comment_validation(comments):
                        break
                    else:
                        print("try again!\n")
                
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


# get web/app name
def get_app_name():
    # Get website/app name
    while True:
        app_name_val = input("\nEnter website or application name: ")
        # Website/App name validation
        if appname_validation(app_name_val):
            break
        else:
            print("try again!\n")
    return app_name_val




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


# Comment Validation
# Return True if Comment is valid
def Comment_validation(cmnt_val):
    is_comnt_valid = False
    print(cmnt_val)
    
    # Check if comment is left empty or user enters space instead of characters
    if not(not(cmnt_val and not cmnt_val.isspace())):

        # Check if comment lenght is more than 30 letters
        if (len(cmnt_val) > 150):
            print("-> More than 150 letters,", end=' ')
        else:
            is_comnt_valid = True
    else:
        print("-> it should not leave empty,", end=' ')
    
    return is_comnt_valid


if __name__ == "__main__":
    print("\nGet Info:\n")
    get_info(2)