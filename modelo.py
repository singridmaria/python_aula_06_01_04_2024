import sqlite3

class AppBD():
    def __init__(self):
        self.create_table()

    def abrirConexao(self):
        try:
            self.connection = sqlite3.connect('database.db')
        except sqlite3.Error as error:
            if(self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)

    def create_table(self):
        self.abrirConexao()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
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

    #FUNÇÃO PARA INSERIR DADOS

    def inserirDados(self,name,price):
        self.abrirConexao()
        insert_query = """INSERT INTO products (name,price) VALUES (?,?)"""

        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query,(name,price))
            self.connection.commit()
            print("Produto inserido com sucesso")
        except sqlite3.Error as error:
            print("Falha ao inserir dados", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechada")

    #FUNÇÃO PARA SELECIONAR TODOS OS DADOS
                
    def select_all_products(self):
        self.abrirConexao()
        select_query = "SELECT * FROM products"
        products = []
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query)
            products = cursor.fetchall()
        except sqlite3.Error as error:
            print("Falha ao selecionar dados", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechada")
        return products

    #FUNÇÃO PARA ATUALIZAR OS DADOS
    
    def update_products(self,product_id,name,price):
        self.abrirConexao()
        update_query = """UPDATE products SET name = ?, price = ? WHERE id = ?"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_query,(name,price,product_id))
            self.connection.commit()
            print("Produto atualizado com sucesso")
        except sqlite3.Error as error:
            print("Falha ao atualizar dados", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechada")

    #FUNÇÃO PARA DELETAR OS DADOS

    def delete_products(self,product_id):
        self.abrirConexao()
        delete_query = """DELETE FROM products WHERE id = ?"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(delete_query,(product_id))
            self.connection.commit()
            print("Produto deletado com sucesso")
        except sqlite3.Error as error:
            print("Falha ao deletar dados", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechada")
