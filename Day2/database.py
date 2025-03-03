import mysql.connector 
conn=mysql.connector.MySQLConnection(
    host="localhost",
    username="mohamed",
    password="Mohamed@8112001",
    database="test"
)

cursor = conn.cursor()

cursor.execute("select *from trainee ;")
values = cursor.fetchall()
print(f"Connected to mysql: {values[0]}")

# Close connection
cursor.close()
conn.close()