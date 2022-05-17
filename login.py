import sqlite3
from getpass import getpass

connector = sqlite3.connect("loginsys.db")
cur = connector.cursor()

"""
uncomment this line below to create a table for storing data and after that, comment it back again
"""
"""
cur.execute("CREATE TABLE user (username, email, password, confirm_password)")

connector.commit()
"""

connector.row_factory = sqlite3.Row

curr = connector.execute("SELECT email, password FROM user")


def signup():
	username = input("Enter Username: ")
	email = input("Enter Email: ")
	password = getpass("Enter Password: ")
	confirm_password = getpass("Confirm Password: ")
	db_email = ""
	for row in curr:
		if row["email"] == email:
			print("Email already in use")
			print()
			signup()	
	
	if password == confirm_password:
		connector.execute("INSERT INTO user VALUES (?, ?, ?, ?)", (username, email, password, confirm_password))
		connector.commit()
		print("Account successfully created")
	else:
		print("Passwords do not match")
		signup()


def login():
	email = input("Enter Email: ")
	password = getpass("Enter Password: ")
	db_email = ""
	db_password = ""
	for row in curr:
		if row["email"] == email:
			db_email += row["email"]
			db_password += row["password"]
			break
	
	if password == db_password:
		print("Login success")
	else:
		print("Incorrect username or password")
		print()
		login()
	

if __name__ == "__main__":
	response = input("Press 0 to signup and 1 to login: ")
	if response == "0":
		signup()
	elif response == "1":	
		login()
	else:
		print("Invalid Input")
connector.close()