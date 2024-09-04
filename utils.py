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

        #frame inicial - superior
        self.frame_superior=Frame_Superior(self,width=1100,height=80)
        self.frame_superior.grid(row=0,column=0)

        #frame tabview - meio
        self.frame_button_tablet=Frame_Button_Tablet(self,width=1100, height=800)
        self.frame_button_tablet.grid(row=1,column=0)


        #frame resposta - inferior

        



        

  
#criando uma classe com frame superio
class Frame_Superior(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.label_nome=ctk.CTkLabel(master,text="Aplicativo Desenvolvido para Auxiliar no Monitoramento da Qualidade do Ar na cidade de João Pessoa",font=("Arial bold",20),width=1100,height=65)
        self.label_nome.grid(row=0,column=0)
        self.label_nome.grid_columnconfigure(0,weight=1)

        


#criando classe com frame para receber a tabview - meio
class Frame_Button_Tablet(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
                
        self.table_view = cadast.Table_View(master=self,width=1100, height=350)
        self.table_view.grid(row=0,column=0)
    


    


