# Não há de fato Variáveis Constantes no Python. Mas podemos declarar em MAIÚSCULO para simbolzar constantes

# Entrada de Dados
# nome        = input("Digite o seu nome: ")
# nascimento  = input("Qual seu nome de nascimento? ")
# email       = input("Digite seu e-mail: ")
# print("Meu nome é : ", nome, " meu ano de nascimento é: ", nascimento, " e meu e-mail é: ", email)

#Tratamento de números no input
from math import sqrt


a = int(input("Digite um número: "))
print(a + 5)

#1 Operadores Aritiméticos
## +   -   *   /

#2 Operadores Relacionais
## <   >   >=   <=   ==   !=   ===

#2 Operadores Lógicos
## &&   ||    !

#4 Outros Operadores
## potência **
## raiz sqtr()
## modulo (resto) %

print(18%4)

print(sqrt(4))

# ---------------------- CONDICIONAIS -------------------------
# IF / ELIF / ELSE
idade = int(input("Digite a sua idade: "))

if idade > 18:
    print("É maior de idade")
elif idade == 18:
    print("Gerreiro Jedi")
else:
    print("É menor de idade")

#Condição Ternário
print("É maior") if idade >= 18 else print("É menor")

#Switch Case (Match)
a = "Márcio"

match a:
    case "Antonio":
        print("Não é Márcio")
    case "Márcio":
        print("Achou o Márcio")
        sobrenome = input("Digite o seu sobrenome: ")
    case "Pedro":
        print("É Pedro e não Márcio")

# ---------------------- CONDICIONAIS -------------------------

a = 1
b = 0
while a <= b:
    print(b)
    a += 1

a = 1
b = 10
while a <= b:
    print(a, end=" OK")
    a += 1