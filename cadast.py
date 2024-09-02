import customtkinter as ctk
import tkinter.messagebox as mensagem

#criando uma classe tableView 
class Table_View(ctk.CTkTabview):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
                   
        #adicionando as abas
        self.add("Cadastrar Ponto de Coleta")       
        self.add("Registrar e Calcular IQar")

        #ajustando o peso das colunas e linhas no grid - alinhamento em tela
        self.tab("Registrar e Calcular IQar").grid_columnconfigure(0,weight=1)
        self.tab("Registrar e Calcular IQar").grid_columnconfigure(1,weight=0)
        self.tab("Registrar e Calcular IQar").grid_columnconfigure(2,weight=0)
        self.tab("Registrar e Calcular IQar").grid_columnconfigure(3,weight=0)
        self.tab("Registrar e Calcular IQar").grid_columnconfigure(4,weight=0)
        self.tab("Registrar e Calcular IQar").grid_columnconfigure(5,weight=0)

        ######adicioando os elementos da aba Cadastrar ponto 
        self.label_cod_point=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Ponto de Coleta:",anchor="e",width=100,height=20,font=("Arial",15),padx=2,pady=10)
        self.label_cod_point.grid(row=0,column=0)
        self.entry_cod_point=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=25,justify="right")
        self.entry_cod_point.grid(row=0,column=1)
        
        self.label_estado=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Estado:",anchor="e",width=100,height=30,font=("Arial",15),padx=2,pady=10)
        self.label_estado.grid(row=1,column=0)
        self.entry_estado=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=25,justify="right")
        self.entry_estado.grid(row=1,column=1)

        self.label_municipio=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Municipio:",anchor="e",width=100,height=20,font=("Arial",15),padx=2,pady=10)
        self.label_municipio.grid(row=2,column=0)
        self.entry_municipio=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=25,justify="right")
        self.entry_municipio.grid(row=2,column=1)
        
        self.label_bairro=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Bairro:",anchor="e",width=100,height=20,font=("Arial",15),padx=2,pady=10)
        self.label_bairro.grid(row=3,column=0)
        self.entry_bairro=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=25,justify="right")
        self.entry_bairro.grid(row=3,column=1)

        self.label_ref=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Referencia:",anchor="e",width=100,height=20,font=("Arial",15),padx=2,pady=10)
        self.label_ref.grid(row=4,column=0)
        self.entry_ref=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=50,justify="right")
        self.entry_ref.grid(row=4,column=1)

        self.button_cadast_point=ctk.CTkButton(self.tab("Cadastrar Ponto de Coleta"),text="Cadastrar Local no BD",width=200,height=30,command=self.cadastrar)
        self.button_cadast_point.grid(row=5,column=0,columnspan=2,padx=20,pady=20)

    ############
        #adicionando elementos na aba "Registrar e Calcular IQar"
        

    ###############
        #radiobox selecionando qual valores de limites na legislção
        selection = ctk.IntVar(value=0) # uma variavel no sistema que recebe apenas inteiro, e pode ser chamada dentro do radioButton
        
        #combobox para selecionar em qual ponto adicionar os dados
        dados=["deu certo", "não sei"]
        self.combo_box=ctk.CTkComboBox(self.tab("Registrar e Calcular IQar"),width=100,height=40,values=dados)
        self.combo_box.grid(row=5,column=0,ipadx=1)

        #função que altera o limite para o calculo de IQar na legislação - atualmente so esta definido o limete 1- o programa pronto para receber os demais
        def selection_radio_button(self):
            self.limite_1=[]

        #inserção de escolha por radiobox
        self.radio_p1=ctk.CTkRadioButton(self.tab("Registrar e Calcular IQar"),width=60,height=30,text="Padrão de Qualidade PI-1",font=("Arial",15),variable=selection,value=1,command=selection_radio_button)
        self.radio_p1.grid(row=0,column=0)

        self.radio_p2=ctk.CTkRadioButton(self.tab("Registrar e Calcular IQar"),width=60,height=30,text="Padrão de Qualidade PI-2",font=("Arial",15),variable=selection,value=2,command=selection_radio_button)
        self.radio_p2.grid(row=1,column=0)

        self.radio_p3=ctk.CTkRadioButton(self.tab("Registrar e Calcular IQar"),height=30,text="Padrão de Qualidade PI-3",font=("Arial",15),value=3,variable=selection,command=selection_radio_button)
        self.radio_p3.grid(row=2,column=0)

        self.radio_p4=ctk.CTkRadioButton(self.tab("Registrar e Calcular IQar"),width=60,height=30,text="Padrão de Qualidade PI-4",font=("Arial",15),value=4,variable=selection,command=selection_radio_button)
        self.radio_p4.grid(row=3,column=0)      
    ##################
        
          








        #label e entry dos dados
        
        self.label_mp10=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="Material Particulado MP-10",anchor="w",width=100,height=20,font=("Arial",15),padx=5,pady=10)
        self.label_mp10.grid(row=0,column=2)
        self.entry_mp10=ctk.CTkEntry(self.tab("Registrar e Calcular IQar"),height=25,justify="right")
        self.entry_mp10.grid(row=0,column=3,padx=5,pady=10)
        self.iqar_mp10=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="",bg_color="blue",width=100)
        self.iqar_mp10.grid(row=0,column=4)

        self.label_mp25=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="Material Particulado MP-2,5",anchor="w",width=100,height=20,font=("Arial",15),padx=2,pady=10)
        self.label_mp25.grid(row=1,column=2)
        self.entry_mp25=ctk.CTkEntry(self.tab("Registrar e Calcular IQar"),height=25,justify="right")
        self.entry_mp25.grid(row=1,column=3,padx=5,pady=10)
        self.iqar_mp25=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="",bg_color="blue",width=100)
        self.iqar_mp25.grid(row=1,column=4)
        
        self.label_o3=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="                  Ozônio - O3",anchor="w",height=20,font=("Arial",15),padx=2,pady=10)
        self.label_o3.grid(row=2,column=2)
        self.entry_o3=ctk.CTkEntry(self.tab("Registrar e Calcular IQar"),height=25,justify="right")
        self.entry_o3.grid(row=2,column=3,padx=5,pady=10)
        self.iqar_o3=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="",bg_color="blue",width=100)
        self.iqar_o3.grid(row=2,column=4)

        self.label_co=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="Monóxido de Carvono - CO",anchor="w",width=100,height=20,font=("Arial",15),padx=2,pady=10)
        self.label_co.grid(row=3,column=2)
        self.entry_co=ctk.CTkEntry(self.tab("Registrar e Calcular IQar"),height=25,justify="right")
        self.entry_co.grid(row=3,column=3,padx=5,pady=10)
        self.iqar_co=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="",bg_color="blue",width=100)
        self.iqar_co.grid(row=3,column=4)

        self.label_no2=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="Dióxido de Nitrogênio - NO2",anchor="w",width=100,height=20,font=("Arial",15),padx=2,pady=10)
        self.label_no2.grid(row=4,column=2)
        self.entry_no2=ctk.CTkEntry(self.tab("Registrar e Calcular IQar"),height=25,justify="right")
        self.entry_no2.grid(row=4,column=3,padx=5,pady=10)
        self.iqar_no2=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="",bg_color="blue",width=100)
        self.iqar_no2.grid(row=4,column=4)

        self.label_so2=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="Dióxido de Enxofre - SO2",anchor="w",width=100,height=20,font=("Arial",15),padx=2,pady=10)
        self.label_so2.grid(row=5,column=2)
        self.entry_so2=ctk.CTkEntry(self.tab("Registrar e Calcular IQar"),height=25,justify="right")
        self.entry_so2.grid(row=5,column=3,padx=5,pady=10)
        self.iqar_so2=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="",bg_color="blue",width=100)
        self.iqar_so2.grid(row=5,column=4)
      

        self.calc_iqar=ctk.CTkButton(self.tab("Registrar e Calcular IQar"),text="CALCULAR O VALOR DE IAar",command=self.calc_iqar)
        self.calc_iqar.grid(row=6,column=3)

        #criando dicionario com as labels
        self.dic_label_iqar_result={"mp_10":self.iqar_mp10,"mp_25":self.iqar_mp25,"o3":self.iqar_o3,"co":self.iqar_co,"no2":self.iqar_no2,"so2":self.iqar_so2}





    #função para capturar os dados get do tab cadastrar ponto de coleta ----cadastrar ponto de coleta----
    def cadastrar(self):
        #evitar que seja digitado valores nao inteiros no cod_point e obter o ponto de coleta
        try:
            numero =int(self.entry_cod_point.get()) 
            ponto_coleta=[("cod",int(self.entry_cod_point.get())),("estado",str(self.entry_estado.get())),("municipio",self.entry_municipio.get()),("bairro",self.entry_bairro.get()),("ref",self.entry_ref.get())]
            
            print(f"resulta {ponto_coleta}")

        except ValueError:
            #uma mensagem box - para usar tem que importar tkinter.menssagebox
            mensagem.showinfo("ATENÇÃO!!","O campo Ponto de Coleta deve ser um número inteiro.")
            print("Erro")




    #função para calcular o valor do iqar ----registrar e calcular iqar
    def calc_iqar(self):
       
        #lista com valores de entrada
        lista_entrada=[("mp_10",int(self.entry_mp10.get())),("mp_25",int(self.entry_mp25.get())),("o3",int(self.entry_o3.get())),("co",int(self.entry_co.get())),("no2",int(self.entry_no2.get())),("so2",int(self.entry_so2.get()))]

        #listas com os limites dos parametros - tem que escolher os certos para o calculo
        list_indice=[("Boa",range(0,41)),("Moderada",range(41,81)),("Ruim",range(81,121)),("Muito Ruim",range(121,201)),("Péssima",range(201,1000))]
        mp_10=[("mp10 boa",range(0,51)),("mp10 mod",range(51,101)),("mp10 ruim",range(101,151)),("mp10 mruim",range(151,251)),("mp10 pessima",range(251,1000))]
        mp_25=[("mp25 boa",range(0,26)),("mp25 mod",range(26,51)),("mp25 ruim",range(51,76)),("mp25 mruim",range(76,126)),("mp25 pessima",range(126,1000))]
        o3=[("o3 boa",range(0,101)),("o3 mod",range(101,131)),("o3 ruim",range(131,161)),("o3 mruim",range(161,201)),("o3 pessima",range(201,1000))]
        co=[("co boa",range(0,10)),("co mod",range(10,12)),("co ruim",range(12,14)),("co mruim",range(14,16)),("co pessima",range(16,1000))]
        no2=[("no2 boa",range(0,201)),("no2 mod",range(201,241)),("no2 ruim",range(241,321)),("no2 mruim",range(321,1131)),("no2 pessima",range(1131,5000))]
        so2=[("so2 boa",range(0,21)),("so2 mod",range(21,41)),("so2 ruim",range(41,366)),("so2 mruim",range(366,801)),("so2 pessima",range(801,5000))]

        #lista com os limites - para verificar em loop com todos ao mesmo tempo
        lista_limites=[("mp_10",mp_10),("mp_25",mp_25),("o3",o3),("co",co),("no2",no2),("so2",so2)]
        dict_iqar_result={}
       

        


        ########## falta criar em forma de dicionario on fim para facilitar o bd
        ######dificil mas ta funcionando - falta ajustar o calculo do iqar### 
        ####pega a lista de entrada, depois a de limites e compara se tem parametros como o mesmo nome nas listas, depois verifica em qual intervalo o valor esta
        ##tambem compara na que tem o mesmo nome na teabel ado indice e verifica em qual intervalo esta
        ## separa as concentrações inicial, final e o intervalo inicial e final
        for parametro_ent, valor_ent in lista_entrada:
            for parametro_limit, list_valor_limit in lista_limites:
                if parametro_ent in parametro_limit:
                    for __, intervalo_list_limit in list_valor_limit:
                        if valor_ent in intervalo_list_limit:
                            print(f"Para o parametro {parametro_ent} concentração inicial - {intervalo_list_limit.start} e a concentração final - {intervalo_list_limit.stop-1}")
                    for indice, intervalo_indice in list_indice:
                        if valor_ent in intervalo_indice:
                            print(f"Para o parametro {parametro_ent} o indice inicial - {intervalo_indice.start} e o indice final - {intervalo_indice.stop-1}")
                            a=intervalo_indice.start
                            b=(((intervalo_indice.stop-1)-intervalo_indice.start)/((intervalo_list_limit.stop-1)-intervalo_list_limit.start))
                            c=(valor_ent-intervalo_list_limit.start)
                            iqar=max(0,int((a+b*c)))
                            print(f"Parametro {parametro_ent}, IQar:{iqar}")

                            dict_iqar_result[parametro_ent]=iqar


        print(dict_iqar_result)       

        for chave, value in self.dic_label_iqar_result.items():           
            if chave in dict_iqar_result:
                value.configure(text=str(dict_iqar_result[chave]))
                if dict_iqar_result[chave] in range(0,41):
                    value.configure(bg_color="green")
                if dict_iqar_result[chave] in range(41,81):
                    value.configure(bg_color="yellow")
                if dict_iqar_result[chave] in range(81,121):
                    value.configure(bg_color="light yellow")
                if dict_iqar_result[chave] in range(121,201):
                    value.configure(bg_color="red")
                if dict_iqar_result[chave] in range(201,5000):
                    value.configure(bg_color="purple")

                print("deu certo")
   
               
               
           







    
    #####acessando o banco de dados e criando a tabela de Ponto_coleta



