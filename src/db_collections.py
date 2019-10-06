# Author: Nima Daryabar
# Insert or Retrive data into/from database
import pymongo


""" Insert user account information into database
     and return a boolean as the result
"""
def insert_data(db, account_info, list_len):
    print("\n db: ", db)
    print("\n acc: ", account_info)
    print("\nlen: ", len(account_info))
    print("\n coun: ", list_len)

    account_list_dict = []

    key_name_list = ['appname', 'username', 'password', 'comment']

    # Create dictionary from tuples/tuple in the account list
    for value_item in account_info:
        print("\n", value_item)
        account_dict = dict(zip(key_name_list, value_item))
        print("single dict: ", account_dict)
        if list_len == 1:
            break
        # else:
        account_list_dict.append(account_dict)


    # If there is more than 1 item in the user account list
    if list_len > 1:
        # Using insert_one() to insert item into database
        pass
    # If there is just one dictionary
    else:
        pass     


    print("\n\ndict list: ", account_list_dict)





def retrieve_data(db):
    pass



if __name__ == "__main__":
    print("nima")