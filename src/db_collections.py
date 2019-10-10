# Author: Nima Daryabar
# Insert or Retrive data into/from database
import pymongo
from regcheck import *


# show a list of collections or make a new one
# coll_list_db: db from insert_data()
def collection_list(coll_list_db):
    print("\n List of collections:")
    collectn_list = coll_list_db.list_collection_names()

    # Check if collection list is empty or not to show it to the user
    if not collectn_list:
        print("\n-> There is no collection in database!")
    else:
        for counter, collection_name in enumerate(collectn_list, 1):
            print(counter, '.', collection_name)
    return collectn_list


# create a collection
# create_coll_db: db from insert_data()
# collec_list: collection list from collection_list()
def create_collection(craete_coll_db, collec_list):
    # Check if name exists or not
    coll_name_exists = True
    while coll_name_exists:
        # Get collection name from user
        coll_name_user = input('\nGive a collection name to create one: ')
        print(coll_name_user)

        # if db name exists
        if coll_name_user in collec_list:
            print("\n-> The collection is already created! Enter New name plz!")

        else:
            # Create collection
            coll = craete_coll_db[coll_name_user]
            print("\nCollection is created")
            coll_name_exists = False
    
    return coll


# choose collection from list
# choose_coll_db: db from insert_data()
# choose_coll_list: collection list from collection_list()
def choose_collection(choose_coll_db, choose_coll_list):
    # Check if user enters correct number
    while True:
        # Getting number from user
        print("\nEnter collection list number: ", end=' ')
        coll_list_num = digit_check()

        # Check if number is in the range of db_list length
        if coll_list_num == 0:
            print("Wrong number! again plz!")
            continue
        if coll_list_num in range(len(choose_coll_list)+1):
            break
        else:
            print("Wrong number! plz enter number in a range of 1 to ", len(choose_coll_list))

    print(f"collection: {choose_coll_list[(coll_list_num-1)]}")
    choosen_coll = choose_coll_list[(coll_list_num-1)]  # Get collection name from collection list
    ch_coll = choose_coll_db[choosen_coll] # Get collection from database
    return ch_coll


""" Insert user account information into database
     and return a boolean as the result
"""
def insert_data(db, account_info, list_len):
    print("\n db: ", db)
    print("\n acc: ", account_info)
    print("\nlen: ", len(account_info))
    print("\n coun: ", list_len)

    # List of dictionaries for more than 1 item in account list
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
    
    print("\n\ndict list: ", account_list_dict)

    coll_list = collection_list(db)

    # create collection
    if not coll_list:
        # create one
        new_coll = create_collection(db, coll_list)
        print("\nnew coll: ", new_coll)
    else:
        choosen_collection = choose_collection(db, coll_list)
        print("choosen coll: ", choosen_collection)
        #  choose from list



    # If there is more than 1 item in the user account list
    if list_len > 1:
        # Using insert_one() to insert item into database

        pass
    # If there is just one dictionary
    else:
        # inserted_dctnry = 
        pass



def retrieve_data(db):
    pass



if __name__ == "__main__":
    print("nima")




"""
# Asking user to make a new collection or used one from the list
    # new_db = False
    check_answer_to_make_new_coll = True
    while check_answer_to_make_new_coll:
        answer_new_or_list = input("\nMaking new collection(c) or Using one from list(l) - (c/l): ")
        
        # Making a new databse
        if answer_new_or_list == 'c':
        
        # Using db from old databases in the list
        elif answer_new_or_list == 'l':
            print(answer_new_or_list)


            check_answer_to_make_new_coll = False
            break

        # Wrong answer to make db or use from the list question
        else:
            print("\n*Wrong answer, Enter again plz!")
        
    return coll


"""