import mysql.connector

def connect():
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'projecte')
    return conn

def disconnect(conn):
    conn.close()
