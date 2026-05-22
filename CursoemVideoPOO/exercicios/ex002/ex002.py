# Declaração de classes
class Gafanhotos:
    '''
Essa classe cria um gafanhoto (uma pessoa com nome e idade)

Para criar uma nova pessoa, use
variavel = Gafanhoto( nome, idade)
    '''
    def __init__(self, nome ='Vazio', idade = 0): # Metodo Construtor
        # Atributos de Instancia
        self.nome = nome
        self.idade = idade

    # Metodos de Instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): # Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

# Declaração de objetos

g1 = Gafanhotos("Maria", 17)
g1.aniversario()

print(g1.__dict__) # Attribute
print(g1.__getstate__()) # Method
print(g1.__class__) #Attribute
print(g1.__doc__) # Dunder Attribute
print(g1)