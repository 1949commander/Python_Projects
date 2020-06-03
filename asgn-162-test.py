fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                        'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

for name in (fileList):
    if(name.endswith('txt')):
        print(name)

def data_entry():
    for name in fileList:
        if(name.endswith('txt'))
        cur.execute("INSERT INTO server(sites) VALUES(?)", (name))
    conn.commit()

data_entry()  # ==> call the function
