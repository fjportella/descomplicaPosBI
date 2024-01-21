# Escopo de Função

"""
def soma():
    txt = "Imprimindo resultado com variável"
    return txt

print(soma())


def soma(a, b, d):
    c = a + b + d
    if c % 2 == 0:
        return "Par"
    else:
        return "Impar"
    #return c

print(soma(4, 9, 21))
print(soma(3, 11, 21))
print(soma(4, 10, 21))

"""

"""
# Função recursiva
# Fatorial

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)


print(fatorial(5))

"""

def verificaMaioridade(anoNascimento, anoAtual):

    idade = anoAtual - anoNascimento

    print("Sua idade é: ", idade)

    if idade >=18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")

verificaMaioridade(2016, 2024)
