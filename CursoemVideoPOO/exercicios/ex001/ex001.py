# Declaração de classes
class Gafanhotos:
    def __init__(self): # Metodo Construtor
        # Atributos de Instancia
        self.nome = ""
        self.idade = 0

    # Metodos de Instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de objetos

g1 = Gafanhotos()
g1.nome = 'Maria'
g1.idade = 18
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhotos()
g2.nome = 'Gabriel'
g2.idade = 53
print(g2.mensagem())