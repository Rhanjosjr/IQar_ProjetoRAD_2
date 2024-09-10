import customtkinter as ctk
import tkinter as tk
from tkinter import ttk #treeview esta disponivel no ttk segundo documentação
import tkinter.messagebox as mensagem
import cadast
import tree



from bancoD import Retorno_bd



#criando uma classe principal para criar a janela GUI
class APP(ctk.CTk):
    def __init__(self):
        super().__init__()

#######################
        #janela principal
        self.title("  --  Aplicativo para calcular e armazenar dados de IQar  --  ")
        self.geometry("1200x900")
        self.iconbitmap("IQar.ico")
        self.resizable(False,False)

######################
        # inicial - superior
        self.label_nome=ctk.CTkLabel(self,text="Aplicativo Desenvolvido para Auxiliar no Monitoramento da Qualidade do Ar na cidade de João Pessoa",font=("Arial bold",20),width=1100,height=30)
        self.label_nome.grid(row=0,column=0,padx=50)
        self.label_nome.grid_columnconfigure(0,weight=1)


######################
        # tabview - meio
        self.table_view = cadast.Table_View(master=self,width=1100, height=450)
        self.table_view.grid(row=1,column=0,pady=10,padx=50)

        #atualizar o combobox
        self.table_view.atualiza_combo_box()

#######################
        #frame resposta - inferior
        self.frame_resultado=ctk.CTkFrame(self,width=1100,height=300)
        self.frame_resultado.grid(row=2,column=0,stick="NSEW",padx=50)

        #treeview do banco de dados ponto de coleta e resutlado iqar
        self.tree_view = tree.Tree(self.frame_resultado)
        self.tree_view.grid(row=0,column=0)


        #atualizar e popular treeview ao iniciar o programa - durante a inicialização do objeto
        self.tree_view.atualiza_treeview_ponto()


        #atualiza a e popula a treeview - a instancia viva tabel acessa a função em tree que atualiza o
        self.table_view.tree_atualiza=self.tree_view.atualiza_treeview_ponto

        
#######################

        




          



 
        
                        






        



        


    


    



    


    


