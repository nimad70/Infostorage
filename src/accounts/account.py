# Author: Nima Daryabar
# Get and validate user's account information

# get web/app name
def get_app_name():
    # Check if web/app name is validated
    while True:
        app_name_val = input("\nEnter website or application name: ")
        # Website/App name validation
        if appname_validation(app_name_val):
            break
        else:
            print("try again!\n")
    return app_name_val


# Get username
def get_username():
    # Check if username is validated
    while True:
        username_gu = input("\nEnter username: ")
        # Username validation
        if username_validation(username_gu):
            break
        else:
            print("try again!\n")
    return username_gu


# Get password
def get_password():
    # Check if password is validated
    while True:
        password_gp = input("\nEnter password: ")
        # Password validation
        if password_validation(password_gp):
            break
        else:
            print("try again!\n")
    return password_gp


# Get comments about account information
def get_comments():
    comments_gc = ""
    # Check answer to y/n question about comments
    comments_check_answer = True
    while comments_check_answer:
        # Check if user has any comments about his info
        has_comments = input("\nHave any comments(y/n)? ")

        if has_comments == 'y': # have comments to make
            while True: # check if comment is validated
                comments_gc = input("\nEnter Your comments: ")
                if Comment_validation(comments_gc): # Comment validation
                    break # if True
                else: # comment is not validate
                    print("try again!\n")     
            comments_check_answer = False
            break
        
        elif has_comments == 'n': # no comments to make
            print("Good!")
            comments_check_answer = False
            break
        
        else: # Wrong answer
            print("\nWrong answer to y/n! Enter again plz.")
    return comments_gc


# Website/app name Validation
# Return True if name is valid
def appname_validation(app_val):
    is_app_valid = False
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


# Get user account information
# return info as a list: {[app name, username, password, comments]}
def get_info(item_count):
    account_info = [] # user account information list
    counter_ = 0 # counter to check number of items to get
    while counter_ != item_count:
        print("\nEnter account info number.{}:".format(counter_+1))

        app_name = get_app_name() # Get website/app name
        print("-> app name: {}".format(app_name))

        username_ = get_username() # Get Username
        print(f"-> username: {username_}")
        
        password_ = get_password() # Get Password
        print(f"-> password: {password_}")
        
        comments = get_comments() # Get comments
        print("-> comments: {}".format(comments))

        account_info.append((app_name, username_, password_, comments))
        counter_ += 1

    return account_info


if __name__ == "__main__":
    print("\nGet Info:\n")
    get_info(2)
