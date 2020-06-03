import sqlite3

list_Names = ('information.docx', 'Hello.txt', 'myImage.png', \
                        'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#create a data structure
conn = sqlite3.connect('Asgn_162.db')
c = conn.cursor()

#Create table
c.execute("CREATE TABLE IF NOT EXISTS namesTable( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT,  \
            col_fileName TEXT \
            )")

#Insert links into table
def data_entry():
    for filenames in list_Names:
        if filenames.endswith('txt'):
            c.execute("INSERT INTO namesTable(col_fileName) VALUES(?)", (filenames,))
    conn.commit()

data_entry()  # ==> call the function

#query database
c.execute("SELECT * FROM namesTable")
rows = c.fetchall()
for row in rows:
    print(row)

conn.close()
