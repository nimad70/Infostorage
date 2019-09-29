# Author: Nima Daryabar aka nmdr
# Keeping usernames and password
from db import connect_db


db, new_database = connect_db()
print("\n", db, "\n", new_database)

# Check if user enters the correct letter for retrieving or importing data from/into database
check_retrieve_import = True
while check_retrieve_import:
    answer_retrieve_import = input("\nRetrieve(r) data from database or"
        "Import(i) new data into the database(r/i): ")

    # Retrieving data from database
    if answer_retrieve_import == 'r':
        # Check if user has just created a new database and db is empty
        if new_database:
            print("You've just created a new database, "
                "first you should import some data into database!")
        else:
            print(answer_retrieve_import)

    elif answer_retrieve_import == 'i':
        print(answer_retrieve_import)
        pass

    else:
        print("\n*Wrong answer, Enter again plz!")