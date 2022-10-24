#-------------------------------------------------------------------------------------------------------------------------------
#Ler acessos.
def ler():
    resultado = []
    arq = open("acessos.txt")
    linhas = arq.readlines()
    for linha in linhas:
        resultado.append(linha)
    return resultado

def escrever(lista):
    texto = ''
    for x in lista:
        texto = texto + x
        texto = texto + '\n'
    arquivo = open('tweets.txt','w', encoding="utf-8")
    arquivo.write(texto)
