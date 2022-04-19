from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from senhas import *


def entrar():
    campo_cpf = navegador.find_element(By.CSS_SELECTOR, '#cpf').send_keys(cpf)
    campo_senha = navegador.find_element(By.CSS_SELECTOR, '#txtPassword').send_keys(senha)
    botao_entrar = navegador.find_element(By.CSS_SELECTOR, '#btnEntrar').click()

def sair():
    botao_sair = navegador.find_element(By.CSS_SELECTOR, '#botao_sair').click()
    botao_sim = navegador.find_element(By.XPATH, '//input[contains(@onclick,"window.SIGA.fecharDialogSair(true)")]').click()

i = 0

navegador = webdriver.Chrome()

for x in range(100):
    i += 1
    navegador.get('https://www.siga.univasf.edu.br/univasf/')
    if i == 1:
        entrar()
        sleep(6)
        botao_fechar = navegador.find_element(By.CSS_SELECTOR, '#j_id_jsp_113198226_146\:j_id_jsp_113198226_148').click()
        sair()
    else:
        entrar()
        sleep(3)
        sair()

