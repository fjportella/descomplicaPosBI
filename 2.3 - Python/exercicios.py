# Aula 3

anoNascimento = int(input("Digite seu ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

idade = anoAtual - anoNascimento

print("Sua idade é: ", idade)

if idade >=18:
    print("Você é maior de idade")
    tituloEleitor = input("Digite seu título de eleitor: ")
else:
    print("Você é menor de idade")
    documentoResponsavel = input("Digite o documento do responsável: ")
