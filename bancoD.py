# classe com os dados do banco de dados

import sqlite3 as conector
import tkinter.messagebox as mensagem


comando_criar_tabela_ponto= '''CREATE TABLE IF NOT EXISTS ponto (cod INTEGER NOT NULL,
                                 estado TEXT NOT NULL,
                                     municipio TEXT NOT NULL,
                                        bairro TEXT NOT NULL, 
                                            ref TEXT,
                                                PRIMARY KEY(cod));'''
comando_cadastrar_ponto= '''INSERT INTO ponto(cod, estado, municipio, bairro, ref) VALUES(:cod, :estado, :municipio, :bairro, :ref);'''

comando_criar_tabela_iqar= '''CREATE TABLE IF NOT EXISTS iqar( id INTEGER PRIMARY KEY AUTOINCREMENT,
                            mp_10 INTEGER ,
                                mp_25 INTEGER, 
                                    o3 INTEGER, 
                                        co INTEGER, 
                                            no2 INTEGER,
                                                so2 INTEGER, 
                                                    iqar_dia INTEGER,
                                                        data TEXT,
                                                            cod INTEGER NOT NULL);'''

comando_cadastrar_iqar= '''INSERT INTO iqar(mp_10,mp_25, o3, co, no2, so2, iqar_dia, data, cod) VALUES(:mp_10, :mp_25, :o3, :co, :no2, :so2, :iqar_dia, :data, :cod)'''

#forçar o banco de dados a verificar integridade de chave estrangeira
#comando_considerar_foreign='''PRAGMA foreign_keys = on'''



#lista dos cod da tabela point
list_combo=[]
class Banco_Dados_Ponto():
    def __init__(self) :
        super().__init__()
    
    ###### funçao para criar e cadastrar dados dos pontos de coleta
    def validar(self,ponto_coleta):
        
        try:

            conexao=conector.connect("Banco_Dados.db")
            cursor=conexao.cursor()
            #cursor.execute(comando_considerar_foreign)
            cursor.execute(comando_criar_tabela_ponto)

            cursor.execute(comando_cadastrar_ponto,{"cod":ponto_coleta["cod"],
                                                    "estado":ponto_coleta["estado"],
                                                    "municipio":ponto_coleta["municipio"],
                                                    "bairro":ponto_coleta["bairro"],
                                                    "ref":ponto_coleta["ref"]})
         
            conexao.commit()
            mensagem.showinfo("Atenção","Cadastro de Ponto de coleta realizado com sucesso!")

            #selecionar os dados do atributo cod na tabela ponto

        except conector.DataError as e:
            mensagem.showinfo("Erro",f"Erro ao acessar o banco de dados {e}")
        except conector.Error as e:
            mensagem.showinfo("Erro",f"Erro inesperado {e}")
        finally:
            print("tabela ponto criada")
            cursor.close()
            conexao.close()
       

    ######## função para cadastrar e criar tabela iqar  
    def cadastrar(self,consolidado):

        #iniciar conexão com bd
        try:
            conexao=conector.connect("Banco_Dados.db")
            cursor=conexao.cursor()
            cursor.execute(comando_criar_tabela_iqar)
            #cursor.execute(comando_considerar_foreign)

            cursor.execute(comando_cadastrar_iqar,{"mp_10":consolidado["mp_10"],
                                                    "mp_25":consolidado["mp_25"],
                                                    "o3":consolidado["o3"],
                                                    "co":consolidado["co"],
                                                    "no2":consolidado["no2"],
                                                    "so2":consolidado["so2"],
                                                    "iqar_dia":consolidado["iqar_dia"],
                                                    "data":consolidado["data"],
                                                    "cod":consolidado["cod"]
                                                    })


            conexao.commit()
            mensagem.showinfo("Atenção","Cadastro de IQar realizado com sucesso!")


        except conector.DataError as e:
            mensagem.showinfo("Erro",f"Erro ao acessar o banco de dados {e}")
        except conector.Error as e:
            mensagem.showinfo("Erro",f"Erro inesperado {e}")
        finally:
            print("tabela iqar criada")
            #fecahr conexao com bd
            cursor.close()
            conexao.close()


######### função para atualizr o combobox com os valores do banco de dados
    def list_pontos(self):
        try:
            conexao=conector.connect("Banco_Dados.db")
            cursor=conexao.cursor()
            
            cursor.execute("SELECT cod FROM ponto")
            #metrodo fetchall para obter todos os dados selecionados
            rows = cursor.fetchall()
            #criar uma lista com os resultados

            for row in rows:
                list_combo.append(str(row[0]))
            return list_combo
            
        except conector.Error as e:
            mensagem.showinfo("Erro",f"Erro inesperado {e}")   
        finally:
                       
            cursor.close()
            conexao.close()



######### função para obter os dados do banco de dados ponto   
class Retorno_bd():
    def __init__():
        super().__init__
        
    def retorno_pontos_coleta():
        
        try:
            conexao=conector.connect("Banco_Dados.db")
            cursor=conexao.cursor()

            cursor.execute("SELECT * FROM ponto")
            dados=cursor.fetchall()

        except conector.Error as e:
            mensagem.showinfo("Erro",f"Erro inesperado {e}")   
        finally:
                       
            cursor.close()
            conexao.close()      
    
        return dados
    
    

######### função para obter os dados do banco de dados iqar
    def retorno_iqar(cod):
        
        try:
            conexao=conector.connect("Banco_Dados.db")
            cursor=conexao.cursor()

            #nesse comando sera selecionado apenas os dados com o id selecionado
            cursor.execute("SELECT * FROM iqar WHERE cod=?",(cod,))
            dados=cursor.fetchall()

        except conector.Error as e:
            mensagem.showinfo("Erro",f"Erro inesperado {e}")   
        finally:
                       
            cursor.close()
            conexao.close()
    
        return dados 



        











    









