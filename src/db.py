from pymongo import MongoClient


# Running Mongod instance
client = MongoClient('localhost', 27017)

# Show all available databases
print("databases list:\n")
db_list = client.list_database_names()
for counter, dbname in enumerate(db_list, 1):
    print(counter, '.', dbname)

# print()
# print(db_list[1])

# db_name = input('Give database name: ')

# Create database
# db = client['reg_info_db']

