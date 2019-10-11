# Author: Nima Daryabar
# Insert or Retrive data into/from database
import pymongo
from regcheck import *


# show a list of collections or make a new one
# coll_list_db: db from make_collection()
def collection_list(coll_list_db):
    print("\n List of collections:")
    collectn_list = coll_list_db.list_collection_names()

    # Check if collection list is empty or not to show it to the user
    if not collectn_list:
        print("\n-> There is no collection in database!")
    else:
        for counter, collection_name in enumerate(collectn_list, 1):
            print(counter, '.', collection_name)
    return collectn_list # Return collection list


# create a collection
# create_coll_db: db from make_collection()
# collec_list: collection list from collection_list()
def create_collection(craete_coll_db, collec_list):
    while True: # Check if name exists or not
        while True: # Check if name is only letters
            # Get collection name from user
            coll_name_user = input('\nGive a collection name to create one: ')

            # check if name is only letters
            if check_only_letters(coll_name_user):
                break
            else:
                print("\n -> only letters is allowed")

        # if db name exists
        if coll_name_user in collec_list:
            print("\n-> The collection is already created! Enter New name plz!")
        else:
            # Create collection
            print("coll_name_user: ", coll_name_user)
            coll = craete_coll_db[coll_name_user]
            print("\nCollection is created")
            break
    return coll # Return created collection


# choose collection from list
# choose_coll_db: db from make_collection()
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
            print("Wrong number! plz enter a number in a range of 1 to ", len(choose_coll_list))

    print(f"collection: {choose_coll_list[(coll_list_num-1)]}")
    choosen_coll = choose_coll_list[(coll_list_num-1)]  # Get collection name from collection list
    ch_coll = choose_coll_db[choosen_coll] # Get collection from database
    return ch_coll # Return choosen collection list


# Make a dictionary of user account informations
# account_info_md: account_info from make_collection()
# list_len_md: list_len from make_collection()
def make_dictionary(account_info_md, list_len_md):
    # List of dictionaries for more than 1 item in account list
    account_list_dict = []

    # Create a list of key names for key/value pair dictionary
    key_name_list = ['appname', 'username', 'password', 'comment']

    # Create dictionary from tuples/tuple in the account list
    for value_item in account_info_md:
        print("\nvalue_item: ", value_item)
        account_dict = dict(zip(key_name_list, value_item)) # {'key_name_list':'value_item', ...}
        print("single dict: ", account_dict)
        # If there is just one item, do not create a list of dictionaries 
        if list_len_md == 1:
            break
        account_list_dict.append(account_dict)  
    print("\n\ndict list: ", account_list_dict)
    # Return account_dict with one info or account_list_dict with multiple info's
    return account_dict, account_list_dict 


# Insert user account information into the database
def insert_data():
    pass



def retrieve_data(db):
    pass


# Make collections
# return True/False as result
def make_collection(db, account_info, list_len):
    print("\n db: ", db)
    print("\n acc: ", account_info)
    print("\nlen: ", len(account_info))
    print("\n coun: ", list_len)

    # user account informations dictionary
    data_dict = make_dictionary(account_info, list_len)
    print("data_dict: {}".format(data_dict))

    coll_list = collection_list(db) # Get list of collections

    # create collection
    if not coll_list: # If collection list is empty
        # create one
        new_coll = create_collection(db, coll_list)
        print("\nnew coll: ", new_coll)
    else:
        # Check if user wants to make a new collection or choose one from the list
        while True: 
            make_new_coll_list = input("\nMake(n) new collection or use(l) one from the list(n/l): ")
            # Make new collection
            if make_new_coll_list == 'n':
                new_coll = create_collection(db, coll_list)
                print("\nnew coll: ", new_coll)
                break
            # Choose one collection from collection list
            elif make_new_coll_list == 'l':
                choosen_collection = choose_collection(db, coll_list)
                print("choosen coll: ", choosen_collection)
                break
            # Wrong answer to y/n question
            else:
                print("\nWrong answer! try again.")



        



    # If there is more than 1 item in the user account list
    if list_len > 1:
        # Using insert_one() to insert item into database

        pass
    # If there is just one dictionary
    else:
        # inserted_dctnry = 
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