# import sqlite module
import sqlite3

# function to get all data from database
def get_all_data():

    try:
        # connect to database
        db = sqlite3.connect("app_database.db")
        # print success message
        print("successfully connected to database.")
        # make the cursor
        cr = db.cursor()
        # fetching data from database
        cr.execute("select * from users")
        # assign data fetched to a variable
        results = cr.fetchall()
        # print number of database rows
        print(f"there are {len(results)} rows in the database.")
        # showing data
        print("showing data.")
        # loop on results
        for row in results:
            print(f"UserID => {row[0]},", end=" ")
            print(f"UserName => {row[1]}")
    except sqlite3.Error as er:
        print(f"error reading data {er}")
    finally:
        # closing database
        if(db):
            db.close()
            print("connection to database is closed!")

get_all_data()