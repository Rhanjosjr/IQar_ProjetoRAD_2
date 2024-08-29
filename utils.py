import customtkinter as ctk
import tkinter.messagebox as mensagem
import cadast




#criando uma classe principal para criar a janela GUI
class APP(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.title("  --  Aplicativo para calcular e armazenar dados de IQar  --  ")
        self.geometry("1200x800")
        #self.iconbitmap("IQar.ico")
        self.resizable(False,False)

        #frame inicial
        self.frame_superior=Frame_Superior(self,width=1100,height=80)
        self.frame_superior.grid(row=0,column=0)

        #frame tabview
        self.frame_button_tablet=Frame_Button_Tablet(self,width=1100, height=300)
        self.frame_button_tablet.grid(row=1,column=0)

        #frame resposta

  

#criando uma classe com frame superio
class Frame_Superior(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.label_nome=ctk.CTkLabel(master,text="Aplicativo Desenvolvido para Auxiliar no Monitoramento da Qualidade do Ar na cidade de João Pessoa",font=("Arial bold",20),width=1100,height=65)
        self.label_nome.grid(row=0,column=0)

#criando classe com frame para receber a tabview
class Frame_Button_Tablet(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.table_view = cadast.Table_View(master=self,width=1100, height=300)
        self.table_view.grid(row=0,column=0)


#criando uma classe tableView 
# class Table_View(ctk.CTkTabview):
#     def __init__(self,master,**kwargs):
#         super().__init__(master,**kwargs)
                   
#         #adicionando as abas
#         self.add("Cadastrar Ponto de Coleta")       
#         self.add("Registrar e Calcular IQar")

#         #adicioando os elementos da aba Cadastrar ponto 
#         self.label_cod_point=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Ponto de Coleta:",anchor="e",width=100,height=20,font=("Arial",15),padx=2,pady=10)
#         self.label_cod_point.grid(row=0,column=0)
#         self.entry_cod_point=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=25,justify="right")
#         self.entry_cod_point.grid(row=0,column=1)
        
#         self.label_estado=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Estado:",anchor="e",width=100,height=30,font=("Arial",15),padx=2,pady=10)
#         self.label_estado.grid(row=1,column=0)
#         self.entry_estado=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=25,justify="right")
#         self.entry_estado.grid(row=1,column=1)

#         self.label_municipio=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Municipio:",anchor="e",width=100,height=20,font=("Arial",15),padx=2,pady=10)
#         self.label_municipio.grid(row=2,column=0)
#         self.entry_municipio=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=25,justify="right")
#         self.entry_municipio.grid(row=2,column=1)
        
#         self.label_bairro=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Bairro:",anchor="e",width=100,height=20,font=("Arial",15),padx=2,pady=10)
#         self.label_bairro.grid(row=3,column=0)
#         self.entry_bairro=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=25,justify="right")
#         self.entry_bairro.grid(row=3,column=1)

#         self.label_ref=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Referencia:",anchor="e",width=100,height=20,font=("Arial",15),padx=2,pady=10)
#         self.label_ref.grid(row=4,column=0)
#         self.entry_ref=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=50,justify="right")
#         self.entry_ref.grid(row=4,column=1)

#         self.button_cadast_point=ctk.CTkButton(self.tab("Cadastrar Ponto de Coleta"),text="Cadastrar Local no BD",width=200,height=30,command=self.cadastrar)
#         self.button_cadast_point.grid(row=5,column=0,columnspan=2,padx=20,pady=20)

        

#     def cadastrar(self):

#         try:
#             numero =int(self.entry_cod_point.get()) 
#             ponto_coleta=[("cod",int(self.entry_cod_point.get())),("estado",str(self.entry_estado.get())),("municipio",self.entry_municipio.get()),("bairro",self.entry_bairro.get()),("ref",self.entry_ref.get())]
#         except ValueError:
#             mensagem.showinfo("ATENÇÃO!!","O campo Ponto de Coleta deve ser um número inteiro.")
#             print("Erro")
     
        