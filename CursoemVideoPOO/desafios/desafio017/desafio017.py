from rich import print
from rich.panel import Panel


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return f"{self.nome} Valor: {self.valor:,.2f}"


    def etiqueta(self):
        conteudo = f"{self.nome.center(30,' ')}"
        conteudo += f"{'-' * 30}"
        precof = f"RS{self.valor:,.2f}"
        conteudo += f"{precof.center(30, '.')}"
        etiqueta = Panel(conteudo, title= "Produto", width=34) #34 pq tem 1 de borda e um de espaço cada lado -4 + 30
        print(etiqueta)


p1 = Produto( "GOl 1.8 1987 CL", 11000)
p2 = Produto( "Notebook", 2000)
p3 = Produto( "Mouse", 125.50)


p1.etiqueta()
p2.etiqueta()
p3.etiqueta()