from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import func as f

exe_path = GeckoDriverManager().install()
service = Service(exe_path)
options = Options()
confirm = []
texto = ''


options.add_argument("--incognito")
options.headless = True
browser = webdriver.Firefox(service=service, options=options)
#browser = webdriver.Firefox(service=service)

acessos = f.ler()
login = acessos[0].strip()
senha = acessos[1].strip()
assunto = acessos[2].strip()
confirm = acessos[3].strip()
quantidade = int(acessos[4].strip())

# usuario = input("Usuário do Twitter: ")
# senha = input("Senha do Twitter: ")

browser.get("https://twitter.com/login")
print("Acessou o Twitter...")
sleep(6)

#Tentando entrar com o login
try:
    campo_nome_usuario = browser.find_element(
        by=By.XPATH, value="//input[contains(@name,'text')]")
    campo_nome_usuario.click()
    campo_nome_usuario.send_keys(login)
    campo_nome_usuario.send_keys(Keys.RETURN)
    print("Entrou com o nome de usuário...")
    sleep(3)
except Exception as excpt:
    print(f"Tivemos uma falha: {excpt}")
    browser.quit()
    exit(1)


#Tenta entrar com a senha
try:
    campo_senha = browser.find_element(
        by=By.XPATH, value="//input[contains(@name,'password')]")
    # campo_senha.click()
    campo_senha.send_keys(senha)
    campo_senha.send_keys(Keys.RETURN)
    print("Entrou com a senha de usuário...")
    sleep(1)
except Exception as excpt:
    #Caso não encontre o campo de senha, ele seta o uusario para confirmar o login
    #pois o tweeter pede o login em caso de diversas tentativas de login
    try:
        print('Confirm = ', confirm)
        campo_nome_usuario = browser.find_element(
            by=By.XPATH, value="//input[contains(@name,'text')]")
        campo_nome_usuario.click()
        campo_nome_usuario.send_keys(confirm)
        campo_nome_usuario.send_keys(Keys.RETURN)
        print("Confirmou o login...")
        sleep(1)

        #Em seguida julgando que está na tela em que pede para entrar com a senha, ele vai setar a senha.
        campo_senha = browser.find_element(
            by=By.XPATH, value="//input[contains(@name,'password')]")
        # campo_senha.click()
        campo_senha.send_keys(senha)
        campo_senha.send_keys(Keys.RETURN)
        print("Entrou com a senha de usuário...")
        sleep(1)
    except Exception as excpt:
        print(f"Tivemos uma falha: {excpt}")
        browser.quit()
        exit(1)

#aqui inicia com o get do url da pagina em que quero fazer scraping dos tweets
try:
    browser.get(assunto)
    sleep(1)
    print('inicio do scraping')
    x=1
    #rodo um while de acordo com a quantidade setada no arquivo de acessos.
    while x<=quantidade:
        users = browser.find_elements(by=By.XPATH, value='//div[@data-testid="User-Names"]')
        tweets = browser.find_elements(by=By.XPATH, value='//div[@data-testid="tweetText"]')
        for user,tweet in zip(users,tweets):
            if x<=quantidade:
                user.find_elements(by=By.XPATH, value='//span')
                tweet.find_elements(by=By.XPATH, value='//span')
                texto+='Tweet '
                texto+=str(x)
                texto+='\n'
                texto+='Cabeçalho:\n'
                texto = texto + user.text
                texto+='\n'
                texto+='Texto:\n'
                texto = texto + tweet.text
                texto+= '\n\n'
                x+=1
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(2)
except Exception as excpt:
    print(f"Tivemos uma falha: {excpt}")
    input("Pressione enter para sair...")
    browser.quit()
    print("Fim...")

print("Pronto!")
f.escrever(texto)
input("Pressione enter para sair...")
browser.quit()
print("Fim...")