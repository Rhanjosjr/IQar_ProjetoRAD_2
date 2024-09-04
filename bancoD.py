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

comando_criar_tabela_iqar= '''CREATE TABLE IF NOT EXISTS iqar(cod INTEGER NOT NULL,
                                 mp10 INTEGER ,mp25 INTEGER, o3 INTEGER, 
                                    co INTEGER, no2 INTEGER, so2 INTEGER, 
                                        iqar_dia INTEGER,
                                            PRIMARY KEY(cod), 
                                                FOREIGN KEY(cod) REFERENCES ponto(cod));'''
# comando_cadastrar_iqar=

#forçar o banco de dados a verificar integridade de chave estrangeira
#comando_considerar_foreign='''PRAGMA foreign_keys = on'''




list_combo=[]


class Banco_Dados_Ponto():
    def __init__(self) :
        super().__init__()
    
    ###### funçao para criar e cadastrar dados dos pontos de coleta
    def validar(self,ponto_coleta):
        
        try:

            conexao=conector.connect("Banco_Dados.db")
            cursor=conexao.cursor()
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





        











    









