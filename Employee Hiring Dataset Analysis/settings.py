import mysql.connector as connection
from db import HOST, DATABASE, PASSWORD, USERNAME


def connect_database():
    mydb = connection.connect(host=HOST, port="3306", database=DATABASE, user=USERNAME, passwd=PASSWORD)
    return mydb

def load_records():
    mydb = connect_database()
    cursor = mydb.cursor()
    selectquery = "select * from employee_hiring_dataset_analysis"
    cursor.execute(selectquery)
    records = cursor.fetchall()
    return records