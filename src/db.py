# Author: Nima Daryabar
# Making a database using pymongo
from pymongo import MongoClient


# Connecting to the database
def connect_db():

    # Running Mongod instance
    client = MongoClient('localhost', 27017)

    # Show all available databases
    print("databases list:\n")
    db_list = client.list_database_names()
    for counter, dbname in enumerate(db_list, 1):
        print(counter, '.', dbname)

    # Asking user to make a new db or used one from the list 
    check_answer_to_make_new_db = True
    while check_answer_to_make_new_db:
        print()
        answer_new_or_list = input("Making new datbase(n) or Using one from list(l) - (n/l): ")
        
        # Making a new databse
        if answer_new_or_list == 'n':
            # Getting database name from user
            db_name_user = input('\nGive a database name to create one: ')
            print(db_name_user)
            # Create database
            db = client['reg_info_db']
            print("\nDatabase is created")
            break
        
        # Using db from old databases in the list
        elif answer_new_or_list == 'l':
            print(answer_new_or_list)
            
            # Check if user enters correct number
            check_given_number = True
            while check_given_number:
                # Getting number from user
                db_list_num = int(input("\nEnter database list number: "))
                # Check if number is in the range of db_list length
                if db_list_num in range(1, len(db_list)):
                    check_given_number = False
                    break
                else:
                    print("Wrong number! plz enter number in a range of 1 to ", len(db_list))
            
            print(db_list[(db_list_num-1)])
            choosen_db = db_list[(db_list_num-1)]
            print("choosen:", choosen_db)
            db = client[choosen_db]
            break

        # Wrong answer to make db or use from the list question
        else:
            print("\n*Wrong answer, Enter again plz!")
        
    return db


if __name__ == "__main__":
    conn = connect_db()