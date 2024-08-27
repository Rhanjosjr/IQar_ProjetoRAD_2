import customtkinter as ctk


#criando uma classe principal para criar a janela GUI
class APP(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("  --  Aplicativo para calcular e armazenar dados de IQar  --  ")
        self.geometry("1200x800")
        self.iconbitmap("IQar.ico")
        self.resizable(False,False)

        #frame inicial
        self.frame_superior=Frame_Superior(self,width=1100,height=80)
        self.frame_superior.grid(row=0,column=0)


#criando uma classe com frame 
class Frame_Superior(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.label_nome=ctk.CTkLabel(master,text="Aplicativo Desenvolvido para Auxiliar no Monitoramento da Qualidade do Ar na cidade de João Pessoa",font=("Arial bold",20),width=1100,height=65)
        self.label_nome.grid(row=0,column=0)


#criando frame para receber a tabview
class Frame_Button_Tablet(ctk.CTkFrame):
    def __initi__(self,master,**kwargs):
        super().__init__(master,**kwargs)





     
    