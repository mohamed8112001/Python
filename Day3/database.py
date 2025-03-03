import mysql.connector 
# import mysql.connector

class Database:

    def __init__(self):
        
        self.conn=mysql.connector.MySQLConnection(
            host="localhost",
            user="mohamed",
            password="Mohamed@8112001",
            database="python"
        )
        # return self.cursor.fetchall()

        self.cursor = self.conn.cursor()

    def select(self,sql,params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        return self.cursor.fetchall()    


# print(f"Connected to mysql: {values[0]}")
    def close(self):
        # Close connection
        self.cursor.close()
        self.conn.close()


db=Database()
# print(db.select("select * from intake ;"))