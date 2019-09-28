# Making a database using pymongo
from pymongo import MongoClient


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
    if answer_new_or_list == 'n':
        print(answer_new_or_list)
        break
    elif answer_new_or_list == 'l':
        print(answer_new_or_list)
        break
    else:
        print("\n*Wrong answer, Enter again plz!")
# print()
# print(db_list[1])

# db_name = input('Give database name: ')

# Create database
# db = client['reg_info_db']

