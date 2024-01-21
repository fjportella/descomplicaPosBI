# Listas

"""
a = [1,2,3]
print(a)
print(a[0])
a.append(4)
print(a)

# Tuplas (Lista imutável, mesmo conceito de constantes)

a = (1,2,3)
print(a)
print(a[0])
#a.append(4) #não permite adição, nem remoção, nem alteração

tupla = (1,2,3,4,5,6,7,8,9,0)
if 8 in tupla:
    print("Existe na tupla")
else:
    print("Não existe na tupla")


#Dicionário (é uma lista que possui índices, ou seja, atribui nomes a cada índice)
lista = {"nome": "Márcio", 
         "sobrenome": "Santos"}

print(lista["nome"], lista["sobrenome"])


#Conjutos (estrutura padrão que é aplicada em lista, tuplas)
listaA = {1,3,5,6}
listaB = {2,4,6}

print(set(listaA.intersection(listaB)))
print(set(listaA.difference(listaB)))
print(set(listaA.symmetric_difference(listaB)))


#Tuplas em casos reais

lista=[]

for a in range(5):
    lista.append(input("Nome: "))

print(lista)



def verifica_descomplica(lista, indice=0):
    # Caso base 1: Verificamos todos os elementos
    if indice == len(lista):
        return False
    # Caso base 2: Encontramos "Descomplica"
    if lista[indice] == "Descomplica":
        return "Sim"
    else:
        return "Não"
    # Chamada recursiva para o próximo elemento
    return verifica_descomplica(lista, indice + 1)

# Lista de entrada
lista = []

# Preenchendo a lista com nomes
for a in range(5):
    lista.append(input("Nome: "))

# Verifica se 'Descomplica' está na lista
resultado = verifica_descomplica(lista)

# Imprime o resultado da verificação
print("Descomplica está na lista?" , resultado)

"""


