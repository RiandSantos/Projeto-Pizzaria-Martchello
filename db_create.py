import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_server_connection('localhost', 'root', '')

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

create_database_query = "CREATE DATABASE projeto_pizzaria;"
create_database(connection, create_database_query)

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query_with_date(connection, query, date):
    cursor = connection.cursor()
    try:
        cursor.executemany(query,date)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

create_tables = """
  CREATE TABLE cliente(nome varchar(15) NOT NULL PRIMARY KEY,
                      email varchar(60) NOT NULL,
                      password varchar(30) NOT NULL);


  CREATE TABLE pizzas(id int(4) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    nome varchar(30) NOT NULL,
                    tamanho varchar(10) NOT NULL,
                    tipo varchar(15) NOT NULL,
                    valor int(5) NOT NULL);
"""

connection = create_db_connection('localhost', 'root', '', 'projeto_pizzaria')
execute_query(connection, create_tables)

sql_insert_info = "INSERT INTO pizzas (nome, tamanho, tipo, valor) VALUES (%s, %s, %s, %s)"

sql_insert_date = [('Mussarela', 'G', 'Salgada', 25.00),
                   ('Mussarela', 'M', 'Salgada', 23.00),
                   ('Mussarela', 'P', 'Salgada', 20.00),
                   ('Calabresa', 'G', 'Salgada', 26.00),
                   ('Calabresa', 'M', 'Salgada', 24.00),
                   ('Calabresa', 'P', 'Salgada', 21.00),
                   ('Quatro Queijos', 'G', 'Salgada', 28.00),
                   ('Quatro Queijos', 'M', 'Salgada', 26.00),
                   ('Quatro Queijos', 'P', 'Salgada', 23.00),
                   ('Brasileira', 'G', 'Salgada', 30.00),
                   ('Brasileira', 'M', 'Salgada', 28.00),
                   ('Brasileira', 'P', 'Salgada', 25.00),
                   ('Portuguesa', 'G', 'Salgada', 29.00),
                   ('Portuguesa', 'M', 'Salgada', 27.00),
                   ('Portuguesa', 'P', 'Salgada', 24.00),
                   ('Moda da Casa', 'G', 'Salgada', 35.00),
                   ('Moda da Casa', 'M', 'Salgada', 33.00),
                   ('Moda da Casa', 'P', 'Salgada', 30.00),
                   ('Banana com canela', 'G', 'Doce', 32.00),
                   ('Banana com canela', 'M', 'Doce', 30.00),
                   ('Banana com canela', 'P', 'Doce', 27.00),
                   ('Chocolate com morango', 'G', 'Doce', 35.00),
                   ('Chocolate com morango', 'M', 'Doce', 32.00),
                   ('Chocolate com morango', 'P', 'Doce', 30.00)]

connection = create_db_connection("localhost", "root", '', 'projeto_pizzaria')
execute_query_with_date(connection, sql_insert_info, sql_insert_date)
