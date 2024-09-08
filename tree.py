import tkinter as tk
from tkinter import ttk
import os
from bancoD import Retorno_bd

#criando uma classe para o treeview
class Tree(ttk.Treeview):
    def __init__(self,parent):
        super().__init__(parent)

     #treeview dos pontos de coleta
        self.my_tree=ttk.Treeview(self,columns=("Cod","Estado","Municipio","Bairro","Referência"),show="headings",height=17)
        self.my_tree.column("Cod",width=60,minwidth=25,anchor="center")
        self.my_tree.column("Estado",width=60,minwidth=25,anchor="center")
        self.my_tree.column("Municipio",width=70,minwidth=25,anchor="center")
        self.my_tree.column("Bairro",width=100,minwidth=25,anchor="center")
        self.my_tree.column("Referência",width=175,minwidth=25,anchor="w")
        
        self.my_tree.heading("Cod", text="Cod")
        self.my_tree.heading("Estado", text="Estado")
        self.my_tree.heading("Municipio", text="Municipio")
        self.my_tree.heading("Bairro", text="Bairro")
        self.my_tree.heading("Referência", text="Referência")

        self.my_tree.grid(row=0, column=0,pady=10,padx=10,stick="NSEW")

        #retorno de dados do banco de dados para a treeview my_tree
        #tem que verificar se o banco de dados existe
        #função atualizar my_tree

    #treeview do iqar
        self.my_tree_iqar=ttk.Treeview(self,columns=("mp_10","mp_25","o3","co","no2","so2","iqar_dia","data","cod"),show="headings",height=17)
        self.my_tree_iqar.column("mp_10",width=65,minwidth=25,anchor="center")
        self.my_tree_iqar.column("mp_25",width=65,minwidth=25,anchor="center")
        self.my_tree_iqar.column("o3",width=65,minwidth=25,anchor="center")
        self.my_tree_iqar.column("co",width=65,minwidth=25,anchor="center")
        self.my_tree_iqar.column("no2",width=65,minwidth=25,anchor="center")
        self.my_tree_iqar.column("so2",width=65,minwidth=25,anchor="center")
        self.my_tree_iqar.column("iqar_dia",width=65,minwidth=25,anchor="center")
        self.my_tree_iqar.column("data",width=65,minwidth=25,anchor="center")
        self.my_tree_iqar.column("cod",width=65,minwidth=25,anchor="center")        
        
        self.my_tree_iqar.heading("mp_10", text="Mp 10")
        self.my_tree_iqar.heading("mp_25", text="Mp 2,5")
        self.my_tree_iqar.heading("o3", text="O3")
        self.my_tree_iqar.heading("co", text="CO")
        self.my_tree_iqar.heading("no2", text="NO2")
        self.my_tree_iqar.heading("so2", text="SO2")
        self.my_tree_iqar.heading("iqar_dia", text="IQar_dia")
        self.my_tree_iqar.heading("data", text="Data")
        self.my_tree_iqar.heading("cod", text="Cod")

        self.my_tree_iqar.grid(row=0,column=1,padx=10,pady=10,sticky="NSEW")

        #ativa um evento que atualiza o treeview do iqar para o ponto selecionado
        self.my_tree.bind("<<TreeviewSelect>>", self.selection_tree_ponto)



###############
    #função para atualizar os dados na treeview
    def atualiza_treeview_ponto(self):
        if os.path.exists("Banco_Dados.db"):
            #apagar os dados existentes
            for item in self.my_tree.get_children():              
                self.my_tree.delete(item)
            #inserir os dados
            rows=Retorno_bd.retorno_pontos_coleta()
            for row in rows:
                self.my_tree.insert("","end",values=(row))



######### evento acionado quando um item e selecionado na my_tree
        #comando para associar item selecionado na treeview ponto  com value
            #vai ser acionado por um evento

    def selection_tree_ponto(self, event):
            #apagar os itens existentes
        for item in self.my_tree_iqar.get_children():              
            self.my_tree_iqar.delete(item)

        #obter a seleção na tree -- [0] recebe o numero na lista
        select_cod = self.my_tree.selection()[0]

        item_id = self.my_tree.item(select_cod,"value")[0] # descobre o item baseado no seu numero na lista e retorna o valor na[coluna 0]
        #acessa função em bd e retorna dados em lista
        rows = Retorno_bd.retorno_iqar(item_id)
        print(rows)
        for row in rows:
            self.my_tree_iqar.insert("","end",values=row)



