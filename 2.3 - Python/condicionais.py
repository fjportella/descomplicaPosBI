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
