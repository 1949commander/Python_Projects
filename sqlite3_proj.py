import sqlite3
connection = sqlite3.connect("test_database.db")

c = connection.cursor()

c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, age INT)")

c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")

##c.execute("DROP TABLE IF EXISTS People")

connection.commit()

with sqlite3.connect("test_database.db") as connect:
    # perform any sql operations using connection here



##Firstly, you no longer need to commit() changes you make; they’re automatically saved. Using "with" also helps to handle potential errors and frees up resources that are no longer needed - much like how we can open (and automatically close) files using the "with" keyword.
##
##Keep in mind, however, that you will still need to commit() a change if you want to see the result of that change immediately (before closing the connection).
