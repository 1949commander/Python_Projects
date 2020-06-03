
import sqlite3

conn = sqlite3.connect('name.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                        'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS table_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT,  \
            col_fileName TEXT \
            )")
    conn.commit()

conn = sqlite3.connect('name.db')
with conn:
    cur = conn.cursor()
    for x in (fileList):
        if(x.endswith('txt')):
            cur.execute("INSERT INTO table_files(col_fileName) VALUES (?)" , x)
    conn.commit()

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM table_files")
    varFilename= cur.fetchall()
    for item in varFilename:
        msg = " Name: {}".format(item[0])
    print(msg)
    
conn.close

##if __name__ == '__main__':
##    name_Function()
