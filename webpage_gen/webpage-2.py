import html
statement = "Enter Statement"
f = open("index.html", "w")

html = """\
<html>
  <head></head>
  <body>
    <p>
       <br><br><h1>{statement}</h1><br>
    </p>
  </body>
</html>
""".format(statement=statement)
f.write(html)
f.close()
