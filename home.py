#!F:\Python\python.exe
print("Content-Type:text/html\n\n")

import cgi
import database
import mysql.connector

database.createTable()

print("<html>")
print("<head>")
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
print('<title>Login Page</title>')
print(
    '<style>.footer {position: fixed;left: 0;bottom: 0;width: 100%;background-color: #3eb8cb;color: #000000;text-align: center;}</style>')
print("</head>")
print("<body>")

print("<b>Your information are as follow:</b>")
print("<br>")
print("<br>")
print("<br>")
print("<br>")

'''



 

'''

form = cgi.FieldStorage()

fname = form.getvalue("fname")
flast = form.getvalue("lname")
gender = form.getvalue("gender")
age = form.getvalue("age")
userr = form.getvalue("username")
passw = form.getvalue("password")

print("Your first name is: " + fname)
print("<br>")
print("Your last name is: " + flast)
print("<br>")
print("Your age is: " + gender)
print("<br>")
print("Your gender is: " + age)
print("<br>")
print("Your username is: " + userr)
print("<br>")
print("Your password is: " + passw)


def insertData():
    con = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='P@ssw0rd',
        database='schoolDatabase'

    )
    cur = con.cursor()
    add = "INSERT INTO users (firstn,lastn,gender,age,username,password) VALUES (%s,%s,%s,%s,%s,%s)"
    data = fname, flast, gender, age, userr, passw
    cur.execute(add, data)
    con.commit()
    cur.close()
    con.close()
    print(f'<script>alert("Dear {fname}, your are registered now. Thank you")</script>')


insertData()

print("<br>")
print("<br>")
print(
    f"<b> Dear Mr./Mrs. {flast}, You have been added to our system successfully. Please go to login page and using your credentials, login to our system and enjoy our online services</b>")

print("<br>")
print("<br>")
print("<br>")
print('<b><a href="Login.html">Login Here</a></b>')

print('<div class="footer"><p>William Shakespeare Private Institute - All rights reserved 2021</p></div>')

print("</body>")
print("</html>")
