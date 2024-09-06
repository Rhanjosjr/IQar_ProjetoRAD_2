import customtkinter as ctk
import tkinter as tk
from tkinter import ttk #treeview esta disponivel no ttk segundo documentação
import tkinter.messagebox as mensagem
import cadast
import os


from bancoD import Retorno_bd



#criando uma classe principal para criar a janela GUI
class APP(ctk.CTk):
    def __init__(self):
        super().__init__()

#######################
        #janela principal
        self.title("  --  Aplicativo para calcular e armazenar dados de IQar  --  ")
        self.geometry("1200x900")
        #self.iconbitmap("IQar.ico")
        self.resizable(False,False)

######################
        # #frame inicial - superior
        self.label_nome=ctk.CTkLabel(self,text="Aplicativo Desenvolvido para Auxiliar no Monitoramento da Qualidade do Ar na cidade de João Pessoa",font=("Arial bold",20),width=1100,height=30)
        self.label_nome.grid(row=0,column=0,padx=50)
        self.label_nome.grid_columnconfigure(0,weight=1)


######################
        #frame tabview - meio
        self.table_view = cadast.Table_View(master=self,width=1100, height=450)
        self.table_view.grid(row=1,column=0,pady=10,padx=50)

#######################
        #frame resposta - inferior
        self.frame_resultado=ctk.CTkFrame(self,width=1100,height=300)
        self.frame_resultado.grid(row=2,column=0,stick="NSEW",padx=50)





        #treeview dos pontos de coleta
        my_tree=ttk.Treeview(self.frame_resultado,columns=("Cod","Estado","Municipio","Bairro","Referência"),show="headings",height=300)
        my_tree.column("Cod",width=50,minwidth=25,anchor="center")
        my_tree.column("Estado",width=50,minwidth=25,anchor="center")
        my_tree.column("Municipio",width=50,minwidth=25,anchor="center")
        my_tree.column("Bairro",width=50,minwidth=25,anchor="center")
        my_tree.column("Referência",width=200,minwidth=25,anchor="w")
        
        my_tree.heading("Cod", text="Cod")
        my_tree.heading("Estado", text="Estado")
        my_tree.heading("Municipio", text="Municipio")
        my_tree.heading("Bairro", text="Bairro")
        my_tree.heading("Referência", text="Referência")

        my_tree.grid(row=0, column=0,pady=10,padx=10,stick="NSEW")
        

        #retorno de dados do banco de dados para a treeview my_tree
        #tem que verificar se o banco de dados existe
        #função atualizar my_tree
        if os.path.exists("Banco_Dado.db"):
                rows = Retorno_bd.retorno_pontos_coleta()
                for row in rows:
                        my_tree.insert("","end",values=row)
          

        #treeview do iqar
        my_tree_iqar=ttk.Treeview(self.frame_resultado,columns=("mp_10","mp_25","o3","co","no2","so2","iqar_dia","data","cod"),show="headings",height=300)
        my_tree_iqar.column("mp_10",width=75,minwidth=25,anchor="center")
        my_tree_iqar.column("mp_25",width=75,minwidth=25,anchor="center")
        my_tree_iqar.column("o3",width=75,minwidth=25,anchor="center")
        my_tree_iqar.column("co",width=75,minwidth=25,anchor="center")
        my_tree_iqar.column("no2",width=75,minwidth=25,anchor="center")
        my_tree_iqar.column("so2",width=75,minwidth=25,anchor="center")
        my_tree_iqar.column("iqar_dia",width=75,minwidth=25,anchor="center")
        my_tree_iqar.column("data",width=75,minwidth=25,anchor="center")
        my_tree_iqar.column("cod",width=75,minwidth=25,anchor="center")        
        
        my_tree_iqar.heading("mp_10", text="Mp 10")
        my_tree_iqar.heading("mp_25", text="Mp 2,5")
        my_tree_iqar.heading("o3", text="O3")
        my_tree_iqar.heading("co", text="CO")
        my_tree_iqar.heading("no2", text="NO2")
        my_tree_iqar.heading("so2", text="SO2")
        my_tree_iqar.heading("iqar_dia", text="IQar_dia")
        my_tree_iqar.heading("data", text="Data")
        my_tree_iqar.heading("cod", text="Cod")

        my_tree_iqar.grid(row=0,column=1,padx=10,pady=10,sticky="NSEW")


        #retorno de dados do banco de dados para a treeview my_tree
        rows = Retorno_bd.retorno_pontos_coleta()
        for row in rows:
            my_tree.insert("","end",values=row)

######### evento acionado quano um item e selecionado na my_tree
        #comando para associar item selecionado na treeview com value
        def selection_tree_ponto(event):
                #apagar os itens existentes
                for item in my_tree_iqar.get_children():              
                     my_tree_iqar.delete(item)

                #obter a seleção na tree -- [0] recebe o numero na lista
                select_cod = my_tree.selection()[0]
                item_id = my_tree.item(select_cod,"value")[0] # descobre o item baseado no seu numero na lista e retorna o valor na[coluna 0]

                #acessa função em bd e retorna dados em lista
                rows = Retorno_bd.retorno_iqar(item_id)
                for row in rows:
                        my_tree_iqar.insert("","end",values=row)


########## evento ao selecionar item na my_tree
        #chamando um eventos com widgets da treeview 
        my_tree.bind("<<TreeviewSelect>>",selection_tree_ponto)



 
        
                        






        



        


    


    



    


    


