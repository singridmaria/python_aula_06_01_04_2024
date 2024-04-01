import sqlite3

class AppBD():
    def abrirConexao(self):
        try:
            self.connection = sqlite3.connect('database.db')
        except sqlite3.Error as error:
            print("Falha ao se conectar ao banco de dados", error)

    def create_table(self):
        self.abrirConexao()
        create_table_query = """CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
            price REAL NOT NULL);"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_query)
            self.connection.commit()
        except sqlite3.Error as error:
            print("Falha ao criar a tabela", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechada")

    def inserirDados(self):
        self.abrirConexao()
        insert_query = """INSERT INTO product(name,price) VALUES (?,?)"""

        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query,(name,price))
            self.connection.commit()
