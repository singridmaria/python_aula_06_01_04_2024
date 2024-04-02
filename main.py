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

        self.lblNome = tk.Label(self.janela, text="Nome: ")
        self.lblNome.pack()
        self.entryNome = tk.Entry(self.janela)
        self.entryNome.pack()

        self.lblPreco = tk.Label(self.janela, text="Preço: ")
        self.lblPreco.pack()
        self.entryPreco = tk.Entry(self.janela)
        self.entryPreco.pack()



janela = tk.Tk() # Criar janela principal

product_app = PrincipalBD(janela)

janela.title("Bem vindo a aplicação de banco de dados")

janela.geometry("900x700")
janela.mainloop()  

