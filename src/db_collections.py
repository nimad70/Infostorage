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
        # keep the last value and cause problem in insert_data() if we do not make it empty in multi dictionaries
        account_dict = {}
    print("\n\ndict list: ", account_list_dict)
    # Return account_dict with one info or account_list_dict with multiple info's
    return account_dict, account_list_dict 


# Only checks to make a collection or choose one
# db_cmc = db from make_collection()
# coll_list_cmc: collection list from make_collection()
def checkto_make_choose(db_cmc, coll_list_cmc):
    coll = ""
    # create new collection
    if not coll_list_cmc: # If collection list is empty
        coll = create_collection(db_cmc, coll_list_cmc) # create collection
        print("\nnew coll: ", coll)
    else:
        # Check if user wants to make a new collection or choose one from the list
        while True: 
            make_new_coll_list = input("\nMake(n) new collection or use(l) one from the list(n/l): ")
            
            if make_new_coll_list == 'n': # Make new collection
                coll = create_collection(db_cmc, coll_list_cmc)
                print("\nnew coll: ", coll)
                break
            
            elif make_new_coll_list == 'l': # Choose one collection from collection list
                coll = choose_collection(db_cmc, coll_list_cmc)
                print("choosen coll: ", coll)
                break
            
            else: # Wrong answer to y/n question
                print("\nWrong answer! try again.")

    return coll # return new or choosen collection


# Insert user account information into the database
# list_dict: list_data_dict from make_collection() - list of dictionaries 
# single_dict: single_data_dict from make_collection() - dictionary with one item
# collec: collection_ from make_collection
# return 'True' if data inserted into the database
def insert_data(single_dict, list_dict, collec):
    insert_res = False
    insert_id = ""

    if single_dict: # if single_dict{} is not empty
        insert_id = collec.insert_one(single_dict)
        print(f"insert id: {insert_id.inserted_id}")
        insert_res = True

    elif list_dict: # else if list_dict[] is not empty
        insert_id = collec.insert_many(list_dict)
        print(f"insert id: {insert_id.inserted_ids}")
        insert_res = True

    else:
        print("Something goes wrong!")
    
    return insert_res



def retrieve_data(db):
    pass


# Make collections
# return True/False as result
def make_collection(db, account_info, list_len):
    print("\n db: ", db)
    print("\n acc: ", account_info)
    print("\nlen: ", len(account_info))
    print("\n coun: ", list_len)

    # Make user account informations dictionary
    single_data_dict = {} # Dictionary with one item
    list_data_dict = [] # List of dictionaries
    single_data_dict, list_data_dict = make_dictionary(account_info, list_len) 
    print("\nsingle data_dict: {}".format(single_data_dict))
    print("\nlist data_dict: {}".format(list_data_dict))

    coll_list = collection_list(db) # Get list of collections
    
    collection_ = checkto_make_choose(db, coll_list)
    print("\n\n\n collection_ : {}".format(collection_))

    # Insert data into the database
    res = insert_data(single_data_dict, list_data_dict, collection_)
    print(f"\nres: {res}")
    


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