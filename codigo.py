#biblioteca focada em automação em python

import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.4 # configura o codigo tado a rodar a cada 0.4 s

# COMANDOS BASICOS DO PYAUTOGUI

#pyautogui.press -> pressionar uma tecla
#pyautogui.click -> clicar
#pyautogui.write -> escrever 
#pyautogui.hotkay -> atalho de teclado (ctrl + c)
#pyautogui.PAUSE = tempo -> definir um intervalo entre a execução do codigo

# 1 - Abrir o sistema da empresa 

pyautogui.press('win')

pyautogui.write("chrome")

pyautogui.press("enter")

link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(1) # usado para fazer uma espera especifica no codigo, fazer o computador esperar 3s.

# 2 - Fazer login no site

pyautogui.click(x=710, y=370, button="left")
pyautogui.write("MeninoPudim@gmail.com")

pyautogui.click(x=695, y=476,button="left")
pyautogui.write("pudimdamimi")

time.sleep(1)
pyautogui.press("enter")

# 3 - Importa a base de dados

tabela = pandas.read_csv("produtos.csv")

print (tabela)


time.sleep(1.5)

# 4 - Cadastrar um produto

# Para cada item dento de uma lista de itens quero q vc execute os passos que eu coloquei aqui
# for item in lista itens

for linha in tabela.index:  # tabela.index = lista com todas as linhas da tabela  # 5 - Repetição

    pyautogui.click(x=701, y=256)

    # Codigo
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo)) # string pra transforma numeros em texto
    pyautogui.press("tab")

    # Marca
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # Tipo
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # Categoria
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))   
    pyautogui.press("tab")

    # Preço unitario 
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # Custo do produto
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # Obs 
    obs = tabela.loc[linha,"obs"]
    if obs != "nan":
        pyautogui.write(str(obs))
    pyautogui.press("tab")


    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.scroll(10000) 






















