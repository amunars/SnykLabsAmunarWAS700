#!F:\Python\python.exe
import mysql.connector
import cgi

print("Content-Type:text/html\n\n")

print("<html>")
print("<head>")
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
print('<title>Email Received</title>')
print('')
print("</head>")

print("<body>")
print("<h1>Your information have been save. We will get back to you soon. Thank you</h1>")
print("<br>")
print("<br>")
print("<br>")
print("<br>")

form = cgi.FieldStorage()

names = form.getvalue("user_name")
emails = form.getvalue("user_email")
messages = form.getvalue("user_message")


def createTable():
    try:
        myDB = mysql.connector.connect(
            host='localhost',
            user='root',
            password='P@ssw0rd',
            database='schoolDatabase'
        )
        my_cursor = myDB.cursor()
        query1 = 'CREATE TABLE IF NOT EXISTS emails (name varchar(20), email varchar(50), message varchar (1000))'
        my_cursor.execute(query1)

    except mysql.connector.Error as error:
        print(format(error))
    finally:
        my_cursor.close()
        myDB.close()


def insertEmails():
    try:
        myDB = mysql.connector.connect(
            host='localhost',
            user='root',
            password='P@ssw0rd',
            database='schoolDatabase'
        )
        my_cursor = myDB.cursor()
        query2 = "INSERT INTO emails (name, email, message) VALUES (%s, %s, %s)"
        userData = (names, emails, messages)
        my_cursor.execute(query2, userData)
        myDB.commit()
    except mysql.connector.Error as error:
        print(format(error))
    finally:
        my_cursor.close()
        myDB.close()


createTable()
insertEmails()


print("</body>")
print("</html>")