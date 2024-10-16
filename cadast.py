import customtkinter as ctk
import tkinter.messagebox as mensagem
import bancoD as bd
import os
import tree


#criando uma classe tableView 
class Table_View(ctk.CTkTabview):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        ########## resultado consolidado dos iqar---para cadastrar no bd
        self.consolidado={}

        #########instancia de tree para que cadast consiga atualizar treeview
        self.tree_atualiza=None
        ##################

        #adicionando as abas
        self.add("Cadastrar Ponto de Coleta")       
        self.add("Registrar e Calcular IQar")

        #ajustando o peso das colunas e linhas no grid - alinhamento em tela
        self.tab("Registrar e Calcular IQar").grid_columnconfigure(6,weight=1)

        ######adicioando os elementos da aba Cadastrar ponto 
        self.label_cod_point=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Ponto de Coleta:",anchor="e",width=100,height=20,font=("Arial",15))
        self.label_cod_point.grid(row=0,column=0,padx=2,pady=15)
        self.entry_cod_point=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=25,justify="right")
        self.entry_cod_point.grid(row=0,column=1)
        
        self.label_estado=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Estado:",anchor="e",width=100,height=30,font=("Arial",15))
        self.label_estado.grid(row=1,column=0,padx=2,pady=15)
        self.entry_estado=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=25,justify="right")
        self.entry_estado.grid(row=1,column=1)

        self.label_municipio=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Municipio:",anchor="e",width=100,height=20,font=("Arial",15))
        self.label_municipio.grid(row=2,column=0,padx=2,pady=15)
        self.entry_municipio=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=25,justify="right")
        self.entry_municipio.grid(row=2,column=1)
        
        self.label_bairro=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Bairro:",anchor="e",width=100,height=20,font=("Arial",15))
        self.label_bairro.grid(row=3,column=0,padx=2,pady=15)
        self.entry_bairro=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=25,justify="right")
        self.entry_bairro.grid(row=3,column=1)

        self.label_ref=ctk.CTkLabel(self.tab("Cadastrar Ponto de Coleta"),text="Referencia:",anchor="e",width=100,height=20,font=("Arial",15))
        self.label_ref.grid(row=4,column=0,padx=2,pady=15)
        self.entry_ref=ctk.CTkEntry(self.tab("Cadastrar Ponto de Coleta"),height=50,justify="right")
        self.entry_ref.grid(row=4,column=1,padx=2,pady=10)

        self.button_cadast_point=ctk.CTkButton(self.tab("Cadastrar Ponto de Coleta"),text="Cadastrar Local no BD",width=200,height=30,command=self.cadastrar)
        self.button_cadast_point.grid(row=5,column=0,columnspan=2,padx=20,pady=20)


        ###### temporario so pra descrever o programa em teste e o responsável, depois substituir pelo logo
        self.frame_description= ctk.CTkFrame(self.tab("Cadastrar Ponto de Coleta"),width=200, height=200)
        self.frame_description.grid(row=0,column=2,rowspan=5,padx=50,sticky="n")

        self.label_description=ctk.CTkLabel(self.frame_description,text="Sistema desenvolvido para auxiliar no cálculo e armazenamento do IQar na cidade de João Pessoa.\n\n\nEsse sistema e um protótipo entregue ao grupo de Pesquisa da Qualidade do Ar na UFPB.\n\nEncontrasse em fase de teste e avaliação",font=("arial",18),anchor="w",justify="left")
        self.label_description.grid(row=0, column=0,pady=50,sticky="w",rowspan=4)

        self.label_procuctor=ctk.CTkLabel(self.frame_description,text="Dev -- Romildo H\nRequisito a Disciplina RAD do curso de ADS - Estácio",font=("arial",10),anchor="e",justify="right")
        self.label_procuctor.grid(row=5, column=0,pady=50,sticky="e")



        #adicionando elementos a aba Registrar e Calcular IQar
        self.date=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="Data",anchor="e",width=100,height=20,font=("Arial",15))
        self.date.grid(row=0, column=1)
        self.entry_date=ctk.CTkEntry(self.tab("Registrar e Calcular IQar"),height=25,justify="right")
        self.entry_date.grid(row=0,column=2)
        
        self.label_mp10=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="Material Particulado MP-10",anchor="w",width=100,height=20,font=("Arial",15))
        self.label_mp10.grid(row=1,column=1)
        self.entry_mp10=ctk.CTkEntry(self.tab("Registrar e Calcular IQar"),height=25,justify="right")
        self.entry_mp10.grid(row=1,column=2,padx=5,pady=10)
        self.iqar_mp10=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="",bg_color="blue",width=100,text_color="black")
        self.iqar_mp10.grid(row=1,column=4)

        self.label_mp25=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="Material Particulado MP-2,5",anchor="w",width=100,height=20,font=("Arial",15),padx=2,pady=10)
        self.label_mp25.grid(row=2,column=1)
        self.entry_mp25=ctk.CTkEntry(self.tab("Registrar e Calcular IQar"),height=25,justify="right")
        self.entry_mp25.grid(row=2,column=2,padx=5,pady=10)
        self.iqar_mp25=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="",bg_color="blue",width=100,text_color="black")
        self.iqar_mp25.grid(row=2,column=4)
        
        self.label_o3=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="                  Ozônio - O3",anchor="w",height=20,font=("Arial",15))
        self.label_o3.grid(row=3,column=1)
        self.entry_o3=ctk.CTkEntry(self.tab("Registrar e Calcular IQar"),height=25,justify="right")
        self.entry_o3.grid(row=3,column=2,padx=5,pady=10)
        self.iqar_o3=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="",bg_color="blue",width=100,text_color="black")
        self.iqar_o3.grid(row=3,column=4)

        self.label_co=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="Monóxido de Carvono - CO",anchor="w",width=100,height=20,font=("Arial",15),padx=2,pady=10)
        self.label_co.grid(row=4,column=1)
        self.entry_co=ctk.CTkEntry(self.tab("Registrar e Calcular IQar"),height=25,justify="right")
        self.entry_co.grid(row=4,column=2,padx=5,pady=10)
        self.iqar_co=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="",bg_color="blue",width=100,text_color="black")
        self.iqar_co.grid(row=4,column=4)

        self.label_no2=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="Dióxido de Nitrogênio - NO2",anchor="w",width=100,height=20,font=("Arial",15),padx=2,pady=10)
        self.label_no2.grid(row=5,column=1)
        self.entry_no2=ctk.CTkEntry(self.tab("Registrar e Calcular IQar"),height=25,justify="right")
        self.entry_no2.grid(row=5,column=2,padx=5,pady=10)
        self.iqar_no2=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="",bg_color="blue",width=100,text_color="black")
        self.iqar_no2.grid(row=5,column=4)

        self.label_so2=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="Dióxido de Enxofre - SO2",anchor="w",width=100,height=20,font=("Arial",15),padx=2,pady=10)
        self.label_so2.grid(row=6,column=1)
        self.entry_so2=ctk.CTkEntry(self.tab("Registrar e Calcular IQar"),height=25,justify="right")
        self.entry_so2.grid(row=6,column=2,padx=5,pady=10)
        self.iqar_so2=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="",bg_color="blue",width=100,text_color="black")
        self.iqar_so2.grid(row=6,column=4)    

        self.calc_iqar=ctk.CTkButton(self.tab("Registrar e Calcular IQar"),text="CALCULAR O VALOR DE IQar",command=self.calcular_iqar)
        self.calc_iqar.grid(row=7,column=2)

        self.iqar_dia=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="",bg_color="blue",width=200,height=200)
        self.iqar_dia.grid(row=1,column=6,sticky="ew",pady=50,padx=50,rowspan=6)

        self.cadatrar_db_result=ctk.CTkButton(self.tab("Registrar e Calcular IQar"),text="Cadastrar o resultado no BD",command=self.cadastrar_result)
        self.cadatrar_db_result.grid(row=6,column=6,sticky="e",padx=50)

        #criar um combo vazio
        self.label_combo_box=ctk.CTkLabel(self.tab("Registrar e Calcular IQar"),text="Selec. Ponto de coleta",font=("Arial",10))
        self.label_combo_box.grid(row=0,column=0)
        self.combo_box=ctk.CTkComboBox(self.tab("Registrar e Calcular IQar"),width=100,height=40,values=[])
        self.combo_box.grid(row=1,column=0)        

    #########
        ##criação e atualização do combobox, usando os pontos cadastrados no banco de dados
        #verificar ao iniciar se o banco de dados ja foi criado e se possui dados para o combobox
    def atualiza_combo_box(self):

        #verifica se existe banco de dados criado
        if os.path.exists("Banco_Dados.db"):
      
            try:
                lista_combo=bd.Banco_Dados_Ponto()
                self.dados=lista_combo.list_pontos()
                if not self.dados:
                    self.dado=[]
            except Exception as e:
                self.dados=[]
        else:
            self.dados=[]



        #atera o combobox criado para os valores filtrados
        self.combo_box.configure(values=self.dados)

        
    ###########criando dicionario com as labels que mudam a cor com valores dos iqar calculado
        self.dic_label_iqar_result={"mp_10":self.iqar_mp10,"mp_25":self.iqar_mp25,"o3":self.iqar_o3,"co":self.iqar_co,"no2":self.iqar_no2,"so2":self.iqar_so2}
        
        


####################################################
    #função para capturar os dados get do tab cadastrar ponto de coleta ---- e para cadastrar ponto de coleta----
    def cadastrar(self):
        #evitar que seja digitado valores nao inteiros no cod_point e obter o ponto de coleta
        try:
            numero =int(self.entry_cod_point.get()) 
            ponto_coleta={"cod":int(self.entry_cod_point.get()),"estado":self.entry_estado.get(),"municipio":self.entry_municipio.get(),"bairro":self.entry_bairro.get(),"ref":self.entry_ref.get()}

            #instancia objeto e atribui um dicionario
            cadastro_banco_dados=bd.Banco_Dados_Ponto()
            #cadastrar os dados no bd
            cadastro_banco_dados.validar(ponto_coleta)


            ###########atualizar o treeview - my_tree em utils-para que fique vazio de novo - vai receber (tree_view.atualiza_treeview_ponto)
            self.tree_atualiza()
            #atualiza o combobox
            self.atualiza_combo_box()
            ############

            #apagar os dados na tela
            #usa o metodo .delete(0,tk.END) - 0 inicio do texto até o final tk.END ------no caso fica ctk.END
            self.entry_cod_point.delete(0,ctk.END)
            self.entry_estado.delete(0,ctk.END)
            self.entry_municipio.delete(0,ctk.END)
            self.entry_bairro.delete(0,ctk.END)
            self.entry_ref.delete(0,ctk.END)                            
                   
        except ValueError:
            #uma mensagem box - para usar tem que importar tkinter.menssagebox
            mensagem.showinfo("ATENÇÃO!!","O campo Ponto de Coleta deve ser um número inteiro.")
            


######################################################
    #função para calcular o valor do iqar ----registrar e calcular iqar
    def calcular_iqar(self):
       
        #####lista com valores de entrada -- colocando uma condição na entrada de dados, para garantir que seja um numero int, devido aos calculos
        ### tem outras formas, dessa ficou uma repetiçao para cada item e ainda calcula
        def validar_entrada(name,entrada):
            try:
                return int(entrada.get())
            except ValueError:
                mensagem.showinfo("Atenção", f"Digite apenas números inteiros nos campos de resultados! Verifique o campo {name}")
    #######################################################
    #diz o nome de cada compo com preenchimento errado, passando pelo metodo acima
        lista_entrada=[("mp_10",validar_entrada("Mp_10",self.entry_mp10)),
                       ("mp_25",validar_entrada("Mp_2,5",self.entry_mp25)),
                       ("o3",validar_entrada("O3",self.entry_o3)),
                       ("co",validar_entrada("CO",self.entry_co)),
                       ("no2",validar_entrada("NO2",self.entry_no2)),
                       ("so2",validar_entrada("SO2",self.entry_so2))]
    #########################################################

        #listas com os limites dos parametros - tem que escolher os certos para o calculo
        list_indice=[("Boa",range(0,41)),("Moderada",range(41,81)),("Ruim",range(81,121)),("Muito Ruim",range(121,201)),("Péssima",range(201,1000))]
        mp_10=[("mp10 boa",range(0,51)),("mp10 mod",range(51,101)),("mp10 ruim",range(101,151)),("mp10 mruim",range(151,251)),("mp10 pessima",range(251,1000))]
        mp_25=[("mp25 boa",range(0,26)),("mp25 mod",range(26,51)),("mp25 ruim",range(51,76)),("mp25 mruim",range(76,126)),("mp25 pessima",range(126,1000))]
        o3=[("o3 boa",range(0,101)),("o3 mod",range(101,131)),("o3 ruim",range(131,161)),("o3 mruim",range(161,201)),("o3 pessima",range(201,1000))]
        co=[("co boa",range(0,10)),("co mod",range(10,12)),("co ruim",range(12,14)),("co mruim",range(14,16)),("co pessima",range(16,1000))]
        no2=[("no2 boa",range(0,201)),("no2 mod",range(201,241)),("no2 ruim",range(241,321)),("no2 mruim",range(321,1131)),("no2 pessima",range(1131,5000))]
        so2=[("so2 boa",range(0,21)),("so2 mod",range(21,41)),("so2 ruim",range(41,366)),("so2 mruim",range(366,801)),("so2 pessima",range(801,5000))]


        #lista com os limites - para verificar em loop com todos ao mesmo tempo - juntei as listas como um item em outra lista
        lista_limites=[("mp_10",mp_10),("mp_25",mp_25),("o3",o3),("co",co),("no2",no2),("so2",so2)]
        dict_iqar_result={}
               


        ##########criar em forma de dicionario on fim para facilitar o bd
        ######dificil mas ta funcionando - iqar### 
        ####pega a lista de entrada, depois a de limites e compara se tem parametros como o mesmo nome nas listas, depois verifica em qual intervalo o valor esta
        ##tambem compara na que tem o mesmo nome na leabel dado indice e verifica em qual intervalo esta
        ## separa as concentrações inicial, final e o intervalo inicial e final
        for parametro_ent, valor_ent in lista_entrada:
            for parametro_limit, list_valor_limit in lista_limites:
                if parametro_ent in parametro_limit:
                    for __, intervalo_list_limit in list_valor_limit:
                        #teste de retorno
                        #if valor_ent in intervalo_list_limit:
                            #print(f"Para o parametro {parametro_ent} concentração inicial - {intervalo_list_limit.start} e a concentração final - {intervalo_list_limit.stop-1}")
                        for indice, intervalo_indice in list_indice:
                            if valor_ent in intervalo_indice:
                                #print(f"Para o parametro {parametro_ent} o indice inicial - {intervalo_indice.start} e o indice final - {intervalo_indice.stop-1}")
                                a=intervalo_indice.start
                                b=(((intervalo_indice.stop-1)-intervalo_indice.start)/((intervalo_list_limit.stop-1)-intervalo_list_limit.start))
                                c=(valor_ent-intervalo_list_limit.start)
                                iqar=max(0,int((a+b*c)))
                                #print(f"Parametro {parametro_ent}, IQar:{iqar}")

                                #dicionaio consolidado dos resultados
                                dict_iqar_result[parametro_ent]=iqar
                                #self.consolidado=dict_iqar_result

        # teste de retorno
        #print(dict_iqar_result)      

        #aplicado para classificar os valores individuais dos iqar 
        cont ={}
        for chave, value in self.dic_label_iqar_result.items():           
            if chave in dict_iqar_result:
               
                value.configure(text=str(dict_iqar_result[chave]))

                if dict_iqar_result[chave] in range(0,41):
                    value.configure(bg_color="green")
                    cont["Boa"]=1

                if dict_iqar_result[chave] in range(41,81):
                    value.configure(bg_color="yellow")
                    cont["Moderada"]=2

                if dict_iqar_result[chave] in range(81,121):
                    value.configure(bg_color="orange")
                    cont["Ruim"]=3

                if dict_iqar_result[chave] in range(121,201):
                    value.configure(bg_color="red")
                    cont["Muito Ruim"]=4

                if dict_iqar_result[chave] in range(201,5000):
                    value.configure(bg_color="purple")
                    cont["Pessimo"]=5
       
       
        #encontra a chave que tenha o menor valor em um dicionario e ajusta a cor e valor do iqar do dia, para o menor do dia monitorado   
        #cont_max pega o maior valor em um dicionario e retorna em cont_max
        cont_max = max(cont, key=cont.get)
        if cont_max == "Boa":
            self.iqar_dia.configure(bg_color="green", text=cont_max, font=("Arial", 50), text_color="black")
        elif cont_max == "Moderada":
            self.iqar_dia.configure(bg_color="yellow", text=cont_max, font=("Arial", 50), text_color="black")
        elif cont_max == "Ruim":
            self.iqar_dia.configure(bg_color="orange", text=cont_max, font=("Arial", 50), text_color="black")
        elif cont_max == "Muito Ruim":
            self.iqar_dia.configure(bg_color="red", text=cont_max, font=("Arial", 50), text_color="black")
        elif cont_max == "Pessimo":
            self.iqar_dia.configure(bg_color="purple", text=cont_max, font=("Arial", 50), text_color="black")

        # Consolidado do resultado iqar
        self.consolidado=dict_iqar_result
        self.consolidado["iqar_dia"]=cont_max
        data=self.entry_date.get()
        self.consolidado["data"]=data
        self.consolidado["cod"]=int(self.combo_box.get())
        # teste de retorno
        # print(self.consolidado)

        

        

    ###################################################
    #função para cadastrar no banco de dados os resultado do iqar
    def cadastrar_result(self):
        #criar instancia
        cadastro_banco_dados_iqar=bd.Banco_Dados_Ponto()
        #criar tabela e cadastrar
        cadastro_banco_dados_iqar.cadastrar(self.consolidado)

        ##
        #apagando os dados na tela pra próximo registro
        self.entry_mp10.delete(0,ctk.END)
        self.entry_mp25.delete(0,ctk.END)
        self.entry_o3.delete(0,ctk.END)
        self.entry_co.delete(0,ctk.END)
        self.entry_no2.delete(0,ctk.END)
        self.entry_so2.delete(0,ctk.END)
        self.entry_date.delete(0,ctk.END)
        self.iqar_dia.configure(text="",bg_color="blue")

        #labels coloridas
        self.iqar_mp10.configure(text="",bg_color="blue")
        self.iqar_mp25.configure(text="",bg_color="blue")
        self.iqar_o3.configure(text="",bg_color="blue")
        self.iqar_co.configure(text="",bg_color="blue")
        self.iqar_no2.configure(text="",bg_color="blue")
        self.iqar_so2.configure(text="",bg_color="blue")
    

 




