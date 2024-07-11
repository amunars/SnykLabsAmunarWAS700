#!F:\Python\python.exe

import mysql.connector
import cgi
import os

print("Content-Type:text/html\n\n")

con = mysql.connector.connect(
   host=os.environ.get('DB_HOST'),
   user=os.environ.get('DB_USER'),
   password=os.environ.get('DB_PASSWORD'),
   database=os.environ.get('DB_DATABASE')
)

form = cgi.FieldStorage()
user = form.getvalue("username")
cur = con.cursor()
cur.execute("SELECT * from students")
users = cur.fetchall()
elements = {}
for uname in users[:]:
    elements.update({uname[4]: uname[5]})
if user in elements.keys():
    print(f'<h4>This username: {user} is in our system</h4>')
    print(f"<h4>Here is your Password for this User {user}: {elements[user]}</h4>")
else:
    print(f"<h3>This user {user} is not in our system</h3>")
    print("<h3>Please enter the correct username</h3>")
    print('<h4><a href="ForgotPassword.html">Forgot Password</a></h4>')
