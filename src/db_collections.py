# Author: Nima Daryabar
# Insert or Retrive data into/from database
import pymongo




# show a list of collections or make a new one
def collection_list():
    pass







""" Insert user account information into database
     and return a boolean as the result
"""
def insert_data(db, account_info, list_len):
    print("\n db: ", db)
    print("\n acc: ", account_info)
    print("\nlen: ", len(account_info))
    print("\n coun: ", list_len)

    # define a list of dictionaries if there is more than 1 item in account list
    account_list_dict = []

    # Create a list of key names for key/value pair dictionary
    key_name_list = ['appname', 'username', 'password', 'comment']

    # Create dictionary from tuples/tuple in the account list
    for value_item in account_info:
        print("\n", value_item)
        account_dict = dict(zip(key_name_list, value_item))
        print("single dict: ", account_dict)

        # If there is just one item, do not create a list of dictionaries 
        if list_len == 1:
            break
        account_list_dict.append(account_dict)


    # If there is more than 1 item in the user account list
    if list_len > 1:
        # Using insert_one() to insert item into database

        pass
    # If there is just one dictionary
    else:
        # inserted_dctnry = 
        pass


    print("\n\ndict list: ", account_list_dict)





def retrieve_data(db):
    pass



if __name__ == "__main__":
    print("nima")