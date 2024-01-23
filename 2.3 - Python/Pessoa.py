# ---------------------- USADO NA AULA DE POO ---------------------------

# CLASSE (inicia com letra maiúscula)
# Atributos são as Variáveis

class Pessoa:
    #em Python não existe Private, Protected. 
    #O Underline já indica para o programador que é um atributo que não pode ser alterado (como se fosse protegido)
    #O duplo Underline já indica para o programador que é um atributo que não pode ser alterado fora da classe (como se fosse privado)
    _nome = "Fernando" 
    #__nome = "Fernando" 
    idade = 47

    # MÉTODOS 
    # É uma função, que executa uma ação

    def exibir(self, nome, idade): #por padrão primeiro declara self, depois os demais atributos
        #print(self.nome) #esse self é equivalente ao this
        #print(self.idade)
        print(nome, idade)

    #Método Construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(self.nome, self.idade)

    #GETTERS E SETTERS
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    
    


