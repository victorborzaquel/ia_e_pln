from selenium import webdriver

from selenium.webdriver.common.by import By

import time

import pandas as pd
 
import requests

# 07/12/2023 -> Acrescentada a biblioteca pyautogui
import pyautogui



#from tags import App

# Leitura de arquivo XLS, como por exemplo PRECATORIOS2022.xls

nomeArq = input('Digite o nome do arquivo "xls" a ser processado: ')
print(nomeArq)
df = pd.read_excel(nomeArq)

#################################################################

service = webdriver.ChromeService(executable_path = 'C:/robot/chromedriver-win64/chromedriver.exe')
browser = webdriver.Chrome(service=service)

browser.get('https://www63.bb.com.br/portalbb/djo/id/IdDeposito,802,4647,4648,0,1.bbx?pk_vid=a8c030459b6e546b1624899559a5e218&pk_vid=a8c030459b6e546b1624899559a5e218&pk_vid=a8c030459b6e546b1624900138a5e218&#8203;&pk_vid=c232b04747645307166878141098691e&pk_vid=c232b04747645307166878141098691e&pk_vid=c232b04747645307166878141098691e')

time.sleep(1.5)

###################### REPETE ENQUANTO HOUVER REGISTRO P/ PROCESSAR ######################

for registro, Orgao_de_Justica in enumerate (df["Orgao_de_ Justica"]): 

#TIPO DE JUSTIÇA (FIXO - ESTADUAL)
   search_input_radio_button = browser.find_element(By.XPATH, '//*[@id="formularioIdDeposito:justica:0"]')
   search_input_radio_button.click()

   time.sleep(0.5)

#PRÉ CADASTRAMENTO (FIXO - PRIMEIRO DEPÓSITO))
   search_input_escolha = browser.find_element(By.XPATH, '//*[@id="formularioIdDeposito:optTipoCadastramento"]')
   search_input_escolha.send_keys('PRIMEIRO DEPÓSITO')

   time.sleep(0.5)

#CONTINUAR
   search_input_continuar = browser.find_element(By.XPATH, '//*[@id="formularioIdDeposito:btnContinuar"]')
   search_input_continuar.click()

   time.sleep(0.5)

#UNIDADE DA FEDERAÇÃO (FIXO - RIO DE JANEIRO) 
   search_input_UF = browser.find_element(By.XPATH, '//*[@id="formulario:comboUf"]')
   search_input_UF.send_keys('RJ - RIO DE JANEIRO')

   time.sleep(0.5)

#TRIBUNAL (FIXO - TRIBUNAL DE JUSTIÇA)
   search_input_tribunal = browser.find_element(By.XPATH, '//*[@id="formulario:cmbTribunal"]')
   search_input_tribunal.send_keys('TRIBUNAL DE JUSTICA')

   time.sleep(0.2)

#COMARCA (FIXO - RIO DE JANEIRO)
   search_input_comarca = browser.find_element(By.XPATH, '//*[@id="formulario:cmbComarca"]')
   search_input_comarca.send_keys('RIO DE JANEIRO')

   time.sleep(0.2)

#CONTINUAR
   search_input_continuar = browser.find_element(By.XPATH, '//*[@id="formulario:botaoContinuar"]')
   search_input_continuar.click()

   time.sleep(0.5)

#ÓRGÃO DE JUSTIÇA (FIXO - DIV PRECATÓRIOS JUDICIAIS)
   search_input_orgao_de_justica = browser.find_element(By.XPATH, '//*[@id="formulario:cmbOrgaos"]')
   search_input_orgao_de_justica.send_keys('DIV PRECATORIOS JUDICIAIS')

   time.sleep(0.5)

#NATUREZA DA AÇÃO (FIXO - PRECATÓRIO)
   search_input_natureza_da_acao = browser.find_element(By.XPATH, '//*[@id="formulario:cmbAcoes"]')
   search_input_natureza_da_acao.send_keys('PRECATORIO')

   time.sleep(0.5)

#NÚMERO DO PROCESSO JUDICIAL (***************** VARIÁVEL ***********************)
   search_input_orgao_de_justica = browser.find_element(By.XPATH, '//*[@id="formulario:numeroProcesso"]')
   search_input_orgao_de_justica.send_keys(df.loc[registro, "Numero_do_Processo_Judicial"])

   time.sleep(0.5)

#VALOR DO DEPÓSITO JUDICIAL (***************** VARIÁVEL ***********************)
   search_input_valor_do_deposito_judicial = browser.find_element(By.XPATH, '//*[@id="formulario:valorDeposito"]')
   # search_input_valor_do_deposito_judicial.send_keys(df.loc[registro, "Valor_do_deposito_ judicial"])

   #************************* TRACE *********************************
   valor = df.loc[registro, "Valor_do_deposito_ judicial"]
   ss = (f'{valor:.2f}')
   search_input_valor_do_deposito_judicial.send_keys(ss)

   #************************ TRACE *********************************

   time.sleep(0.15)

#DEPOSITANTE (FIXO - Réu)
   search_input_depositante = browser.find_element(By.XPATH, '//*[@id="formulario:cmbTipoDepositante"]')
   search_input_depositante.send_keys('Réu')

   time.sleep(0.1)

#NOME AUTOR (***************** VARIÁVEL ***********************)
   search_input_nome_autor = browser.find_element(By.XPATH, '//*[@id="formulario:nomeAutor"]')
   search_input_nome_autor.send_keys(df.loc[registro, "Autor"])

   time.sleep(0.2)

#TIPO DE PESSOA AUTOR (***************** VARIÁVEL ***********************)
   search_input_tipo_de_pessoa_autor = browser.find_element(By.XPATH, '//*[@id="formulario:cmbTipoPessoa"]')

   time.sleep(0.2) 

#SÓ PARA TESTE, VAMOS TER QUE LER DO ARQUIVO EM EXCEL PARA PREENCHER O TIPO DE PESSOA
   pessoaAutor = df.loc[registro, "TIPO_DE_PESSOA_AUTOR"]

   if (pessoaAutor == 'Física') :
   #CPF AUTOR
        search_input_tipo_de_pessoa_autor.send_keys('Física')

   else:
   #CNPJ AUTOR
        search_input_tipo_de_pessoa_autor.send_keys('Jurídica')

   time.sleep(0.5)


#NOME RÉU (***************** VARIÁVEL ***********************) ==> ALTERADO PARA A VERSÃO 4
   search_input_nome_reu = browser.find_element(By.XPATH, '//*[@id="formulario:nomeReu"]')
   search_input_nome_reu.send_keys(df.loc[registro, "REU"])
  
   time.sleep(0.15)

#TIPO DE PESSOA RÉU (FIXO - Jurídica)
   search_input_tipo_de_pessoa_reu = browser.find_element(By.XPATH, '//*[@id="formulario:cmbTipoPessoaReu"]')

   time.sleep(0.2)

   search_input_tipo_de_pessoa_reu.send_keys('Jurídica')

   time.sleep(0.2) 

# CPF RÉU (***************** VARIÁVEL ***********************) ==> ALTERADO PARA A VERSÃO 3
   search_input_cnpj_reu = browser.find_element(By.XPATH, '//*[@id="formulario:cnpjReu"]')
   search_input_cnpj_reu.send_keys(df.loc[registro, "CNPJ"])

   time.sleep(0.2)

#GERAR ID
   search_input_gerar_id = browser.find_element(By.XPATH, '//*[@id="formulario:btnGerarID"]')
   search_input_gerar_id.click()

   time.sleep(0.5) #5

# ####################### PAUSAR PARA SALVAR ID ##################################################

#GERAR BOLETO
   search_input_gerar_boleto = browser.find_element(By.XPATH, '//*[@id="botaoImprimirBoleto"]')
   search_input_gerar_boleto.click()

   time.sleep(0.5) #5

# 07/12/2023 -> Acrescentado para salvar a url da págica corrente
   guarda_url = browser.current_url

#CONFIRMAR
   search_input_confirmar = browser.find_element(By.XPATH, '//*[@id="formulario:confirmar"]')
   search_input_confirmar.click()

####################### PAUSAR PARA imprimir boleto ##################################################

# 07/12/2023 -> Acrescentado para salvar a guia (documento) em PDF
   time.sleep(3) #5
  
# 07/12/2023 -> "Salvar o documento como" -> (CTRL + S)
   pyautogui.hotkey('ctrl','s')
   time.sleep(3) #5

   autor = df.loc[registro, "Autor"]
   numero_do_processo_judicial = df.loc[registro, "Numero_do_Processo_Judicial"]
   pyautogui.typewrite(numero_do_processo_judicial + " - " + autor + ".pdf")
   time.sleep(5) #5

 # 07/12/2023 -> "SALVAR = <ENTER>" -> (ENTER)
   pyautogui.press('enter')
   time.sleep(5) #5

 # 07/12/2023 -> Retorna a página anterior (antes de vir para a página de impressão)
   browser.get(guarda_url)
   time.sleep(2) #5

####################### PAUSAR PARA imprimir boleto ##################################################

#RETORNAR
   search_input_retornar = browser.find_element(By.XPATH, '//*[@id="formulario:botaoRetornar"]')
#    search_input_retornar = browser.find_element(By.XPATH, '//*[@id="formulario:btnRetornar"]')
   search_input_retornar.click()

   time.sleep(1.2) #8
