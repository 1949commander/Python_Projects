import sqlite3

peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

# execute insert statement for supplied data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)",peopleValues)
    
# select all the first and last names from people over age 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print (row)
















    
##    line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
##    c.execute(line)
### get personal data from user
##firstName = input("Enter your first name: ")
##lastName = input("Enter your last name: ")
##age = int(input("Enter your age: "))
##personData = (firstName, lastName, age)
    ### update table
##c.execute("UPDATE People SET AGE=? WHERE FirstName=? AND LastName=?",
##          (45, 'Luigi', 'Vercotti'))
