import random
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def coletar_dados(cnpj, data):
  ops = Options()
  ops.add_argument('-headless')
  browser = webdriver.Firefox(service=Service(), options=ops)
  browser.set_window_size(800, 800)
  sleep(1)

  browser.get('https://grpfordam.sefin.fortaleza.ce.gov.br/grpfor/pagesPublic/iptu/damIptu/imprimirDamIptu.seam')
  sleep(2)

  site = BeautifulSoup(browser.page_source, 'html.parser')

  radioButtom = browser.find_element(By.ID, 'pmfInclude:cadastroForm:tipoDecorate:j_id334:1')
  radioButtom.click()
  sleep(2)
  #for juridica

  elemento1 = browser.find_element(By.ID, 'pmfInclude:cadastroForm:cpfDec:cnpj')

  elemento1.send_keys(cnpj)

  elemento2 = browser.find_element(By.ID, 'pmfInclude:cadastroForm:dataNascimentolDec:dataNascimentoInputDate') #para elementos
  elemento2.send_keys(data)
  elemento2.send_keys(data)

  buttomPesquisar = browser.find_element(By.ID, 'pmfInclude:cadastroForm:dataNascimentolDec:botaoRecuperarImovelNaoLogado') #para elementos
  buttomPesquisar.click()

  sleep(5)

  return browser.page_source


def coletarDadosPagina(cnpj, data, timeout):
  if timeout == 0:
    return None

  result = coletar_dados(cnpj, data)

  site = BeautifulSoup(result, 'html.parser')
  alerta = site.find('dt', attrs={'class':'alert alert-danger'})
  if alerta:
    mensagem = alerta.find('span', attrs={'class':'rich-messages-label'})
    if "robô" in mensagem.text:
      sleep(5)
      coletarDadosPagina(cnpj, data, timeout - 1)
    else:
      return site
  else:
    return site

def coletarDadosImovel(cnpj, data, timeout):

  site = coletarDadosPagina(cnpj, data, timeout)

  if site == None:
    return [0, cnpj, data]

  dados_imovel = site.find('span', attrs= {'id': 'pmfInclude:cadastroForm:dadosImovel'})

  if dados_imovel:
    dados_imovel_fieldset = dados_imovel.find('fieldset')
    dados_imovel_tds = dados_imovel_fieldset.find_all('td')
    lista_imovel = []
    for dados_imovel_td in dados_imovel_tds[2::3]:
      lista_imovel.append(dados_imovel_td.text)

    return lista_imovel
  else:
    mensagem_texto = ''
    alerta = site.find('dt', attrs={'class':'alert alert-danger'})
    if alerta:
      mensagem = alerta.find('span', attrs={'class':'rich-messages-label'})
      mensagem_texto = mensagem.text

    return [1, cnpj, data, mensagem_texto]
lista_imovel = coletarDadosImovel('05154921755', '21031976', 2)
print(lista_imovel)

import pandas as pd

df = pd.read_excel('lista_fortaleza.xlsx')

lista_nomes = ['Pessoa Jurídica', 'Data Abertura RFB', 'Inscrição', 'Cartografia', 'Localização', 'Correspondência', 'Adquirente']
lista_cnpjs = []
lista_data_abertura = []
lista_inscricao = []
lista_cartografia = []
lista_localizacao = []
lista_correspondencia = []
lista_adquirente = []

lista_erros_tipo_1 = []
lista_erros_tipo_2 = []