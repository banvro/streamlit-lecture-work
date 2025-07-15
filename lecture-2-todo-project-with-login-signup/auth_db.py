import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    port = 3307,
    username = "root",
    password = "1234",
    database = "streamlitproject"
)

csr = conn.cursor()