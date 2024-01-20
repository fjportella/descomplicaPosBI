# ----------------------- Laços de Repetição -----------------------

# WHILE
a = 1
while a < 5:
    print("Teste While")
    a = a + 1

# FOR
# For Simplificada
for a in range(5):
    print("Teste For")

# For Vetor
# Lista
b = ["Márcio", "Larissa", "Benedito", "André"]
for b in b: #imprime a lista
    print(b)

c = "Descomplica"
for c in c: #quebra letra a letra
    print(c)

# ----------------------- Laços de Repetição -----------------------


# ----------------------- Laços de Repetição com Listas Expansivas -----------------------

a1 = []
b1 = 1
print(a1)

while b1 <= 3:
    a1.append(input("Digite o nome de aluno: ")) #adiciona na lista na posição final
    b1 = b1 + 1
print(a1)

# ----------------------- Laços de Repetição com Listas Expansivas -----------------------


# ------------------------- Adicionando e Removendo Itens de Uma Lista ---------------------
a2 = ["Márcio", "Bruna"]
a2.insert(1, "Helen")
print(a2)
a2.remove("Márcio")
print(a2)

# ------------------------- Adicionando e Removendo Itens de Uma Lista ---------------------
