#acessando arquivo local

#-------------------- Habilitando arquivo -----------------------
#conteudo = open("2.3 - Python/teste.txt", "a")
#conteudo.write("\nUma linha qualquer\n")
#conteudo.write("\nSegunda linha\n")
#conteudo.close()
# R = Read
# W = Write
# X = Execute
# A = Append
# R+
# WB
#-------------------- Habilitando arquivo -----------------------

"""
try:
    with open("teste.txt", "a") as conteudo:
        conteudo.write("Uma linha qualquer\n")
except IOError as e:
    print("Ocorreu um erro de I/O:", e)
"""

# ----------------------------- LER ARQUIVOS DA INTERNET ---------------------------
import requests

ler = requests.get("https://wiki.sj.ifsc.edu.br/images/4/4a/Ecoshower.txt")
#print(ler)

#wb escreve como binário (usado para arquivos internet)
with open("2.3 - Python/arquivo001.txt", "wb") as arquivo:
    arquivo.write(ler.content)
# ----------------------------- LER ARQUIVOS DA INTERNET ---------------------------