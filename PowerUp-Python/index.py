import pyautogui
import pandas
import time

linkEmpresa = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'teste@gmail.com'
senha = 'teste123'
tabela = pandas.read_csv('produtos.csv')

# 1- Entrar no sistema da empresa;
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.PAUSE = 1.5

pyautogui.press('win') # apertar tecla windows
pyautogui.write('firefox') # procurar pelo chrome
pyautogui.press('enter') # Abrir o chrome

# Link
pyautogui.write(linkEmpresa)
pyautogui.press('enter') #Entrar no site

#Esperar carregar:
time.sleep(7)

# 2- Fazer Login;

pyautogui.click(x=481, y=372)
pyautogui.write(email) # Digita o Email
pyautogui.press('tab')
pyautogui.write(senha) # Digita a senha

pyautogui.click(x=624, y=534) # Apertar Entrar
time.sleep(3)

# 3- Importar a base de dados;


# 4- Cadastrar um produto;

for linha in tabela.index:

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.click(x=695, y=253)
    #Código
    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')
    # Marca
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    # Tipo
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    # Categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria'])) # Num
    pyautogui.press('tab')
    # preço
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    # Custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    # obs
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    # Enviar o produto.
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(1000)
# 5- Repetir isso até acabar a base de dados;