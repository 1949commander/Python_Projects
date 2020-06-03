import sqlite3

list_ = ('information.docx', 'Hello.txt', 'myImage.png', \
                        'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#create a data structure
conn = sqlite3.connect('names_162.db')
c = conn.cursor()

#Create table
c.execute("CREATE TABLE IF NOT EXISTS namesTable( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT,  \
            col_fileName TEXT \
            )")
conn.close()
###Insert links into table
##def data_entry():
##    for item in list_:
##        if(item.endswidth('txt')):
##            c.execute("INSERT INTO server(col_fileName) VALUES(?)", (item))
##    conn.commit()
##
##data_entry()  # ==> call the function
##
###query database
##c.execute("SELECT * FROM server")
##rows = c.fetchall()
##for row in rows:
##    print(row)
##
##conn.close()
