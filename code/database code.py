import sqlite3

conn=sqlite3.connect("account.db")

#create the customer details table
"""conn.execute(CREATE TABLE account_info(Username TEXT, Password TEXT, time INTEGER))"""
vUsername=str(input("Enter username:" ))
vPassword=str(input("Enter password:" ))
conn.execute("INSERT INTO account_info (Username, Password, time) \
             VALUES (?, ?,?)",(vUsername, vPassword,0));

conn.commit()
    