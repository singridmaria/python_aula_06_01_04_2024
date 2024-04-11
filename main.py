import tkinter as tk # importar biblioteca
from tkinter import ttk
import modelo as crud #importando modelo.py

class PrincipalBD():
    def __init__(self,win):
        self.objBD = crud.AppBD()
        self.janela = win

        self.treeProdutos = ttk.Treeview(self.janela,columns=("Código do  produto","Nome","Preço"),show="headings")
        self.treeProdutos.heading("Código do  produto",text= "Código do  produto: ")
        self.treeProdutos.heading("Nome",text= "Nome: ")
        self.treeProdutos.heading("Preço",text= "Preço: ")
        self.treeProdutos.pack()
        self.ExibirTela()
        self.lblNome = tk.Label(self.janela, text="Nome: ")
        self.lblNome.pack()
        self.entryNome = tk.Entry(self.janela)
        self.entryNome.pack()

        self.lblPreco = tk.Label(self.janela, text="Preço: ")
        self.lblPreco.pack()
        self.entryPreco = tk.Entry(self.janela)
        self.entryPreco.pack()
        
        self.btnCadastrar = tk.Button(self.janela, text="Adicionar", command=self.CadastrarProduto)
        self.btnAtualizar = tk.Button(self.janela, text="Atualizar", command=self.AtualizarProduto)
        self.btnExcluir = tk.Button(self.janela, text="Excluir", command=self.ExcluirProduto)

       
        self.btnCadastrar.pack(padx=5, pady=5)
        self.btnAtualizar.pack(padx=5, pady=5)
        self.btnExcluir.pack(padx=5, pady=5)

    
    def ExibirTela(self):
        try:
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            products = self.objBD.select_all_products()
            for product in products:
                self.treeProdutos.insert("",tk.END, values=product)

        except:
            print("Não foi possível exibir os campos.")

    def CadastrarProduto(self):
        try:
            name = self.entryNome.get()
            price = float(self.entryPreco.get())
            self.objBD.inserirDados(name,price)
            self.ExibirTela()
            self.entryNome.delete(0, tk.END)
            self.entryPreco.delete(0, tk.END)
            print("Produto Cadastrado com sucesso!")

        except:
            print("Não foi possível fazer o cadastro")

    def ExcluirProduto(self):
        try:
            selected_item = self.treeProdutos.selection()
            if not selected_item:
                return
            item = self.treeProdutos.item(selected_item)
            print(item)
            product = item['values']
            product_id = product[0]
            self.objBD.delete_products(product_id)
            self.ExibirTela()
            print("Produto excluído com sucesso")
        
        except:
            print("não foi possível excluir")

    def AtualizarProduto(self):
        try:
            selected_item = self.treeProdutos.selection()
            if not selected_item:
                return
            item = self.treeProdutos.item(selected_item)
            print(item)
            product = item['values']
            product_id = product[0]
            nome = self.entryNome.get()
            preco = float(self.entryPreco.get())
            self.objBD.update_products(product_id,nome,preco)
            self.ExibirTela()
            
            self.entryNome.delete(0,tk.END)
            self.entryPreco.delete(0,tk.END)
            print("Produto atualizado com sucesso")
            
        except:
            print("Não foi possível atualizar")
            
            
            







janela = tk.Tk() # Criar janela principal
product_app = PrincipalBD(janela)
janela.title("Bem vindo a aplicação de banco de dados")
janela.geometry("900x700")
janela.mainloop()  

