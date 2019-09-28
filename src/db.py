from pymongo import MongoClient


# Running Mongod instance
client = MongoClient('localhost', 27017)

# Create database
db = client['reg_info_db']

