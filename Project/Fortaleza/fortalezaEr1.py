from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ops = Options()
# ops.headless = False #para nao mostrar o navegador True
print("***")
browser = webdriver.Firefox(options=ops)
browser.set_window_size(800, 800)
sleep(1)

browser.get('https://grpfordam.sefin.fortaleza.ce.gov.br/grpfor/pagesPublic/iptu/damIptu/imprimirDamIptu.seam')
sleep(2)

site = BeautifulSoup(browser.page_source, 'html.parser')

# print(site.prettify())

"""
bottom = browser.find_element(By.ID, 'pmfInclude:cadastroForm:tipoDecorate:j_id334:1')
bottom.click()
sleep(2)
#for juridica 
"""
elemento1 = browser.find_element(By.ID, 'pmfInclude:cadastroForm:cpfDec:cpf') #para elementos

elemento1.send_keys('05154921755')

elemento2 = browser.find_element(By.ID, 'pmfInclude:cadastroForm:dataNascimentolDec:dataNascimentoInputDate') #para elementos
elemento2.send_keys('21031976')
elemento2.send_keys('21031976')

bottom = browser.find_element(By.ID, 'pmfInclude:cadastroForm:dataNascimentolDec:botaoRecuperarImovelNaoLogado') #para elementos
bottom.click()

sleep(5)

page_content = browser.page_source
site = BeautifulSoup(page_content, 'html.parser')
# print (site.prettify())

posts = site.findAll('fieldset')


found = False

for produto in posts:
    # print(produto.prettify())
    table= produto.find_element(By.ID, 'pmfInclude:cadastroForm:dataTable')





# '07836612000168''13061973'
