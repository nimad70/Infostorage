# Author: Nima Daryabar
# Insert or Retrive data into/from database
import pymongo


# show a list of collections or make a new one
def collection_list(db):
    print("\n List of collections:")

    collection_list = db.list_collection_names()

    # Check if collection list is empty or not to show it to the user
    if not collection_list:
        print("\n-> There is no collection in database!")
    else:
        for counter, collection_name in enumerate(collection_list, 1):
            print(counter, '.', collection_name)
    
    return collection_list


def create_collection():
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
    
    print("\n\ndict list: ", account_list_dict)

    coll_list = collection_list(db)

    # create collection
    if not coll_list:
        # create one
        create_collection()
        pass
    else:
        pass
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

            # Check if name exists or not
            coll_name_exists = True
            while(coll_name_exists):
                # Getting database name from user
                coll_name_user = input('\nGive a collection name to create one: ')
                print(coll_name_user)

                # if db name exists
                if coll_name_user in collection_list:
                    print("\n-> The collection is already created! Enter New name plz!")

                else:
                    # Create collection
                    coll = db[coll_name_user]
                    print("\nCollection is created")
                    coll_name_exists = False
                    # new_db = True
                    check_answer_to_make_new_coll = False
                    break
            
        
        # Using db from old databases in the list
        elif answer_new_or_list == 'l':
            print(answer_new_or_list)
            
            # Check if user enters correct number
            check_given_number = True
            while check_given_number:
                # Getting number from user
                coll_list_num = int(input("\nEnter collection list number: "))
                # Check if number is in the range of db_list length
                if coll_list_num in range(1, len(collection_list)):
                    check_given_number = False
                    break
                else:
                    print("Wrong number! plz enter number in a range of 1 to ", len(collection_list))
            
            print(collection_list[(coll_list_num-1)])
            choosen_coll = collection_list[(coll_list_num-1)]
            print("choosen:", choosen_coll)
            coll = db[choosen_coll]
            check_answer_to_make_new_coll = False
            break

        # Wrong answer to make db or use from the list question
        else:
            print("\n*Wrong answer, Enter again plz!")
        
    return coll


"""