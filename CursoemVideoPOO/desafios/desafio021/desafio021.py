from rich import print

class Caneta:
    def __init__(self, cor = "azul"):
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "amarelo" | "amarela":
                escolha = "[yellow]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True

    def escrever(self, msg):
        if self.tampada:
            print(f"\n:prohibited: A {self.cor}caneta[/] está tampada!")
        else:
            print(f"{self.cor}{msg}[/] ", end ='')

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

c1 = Caneta("azul")
c2 = Caneta("vermelho")
c3 = Caneta("amarela")
c4 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Ola Mundo")
c2.escrever("Ola Mundo")
c3.escrever("Ola Mundo")
c4.escrever("Ola Mundo")

c1.tampar()

c1.escrever("Ola Mundo")
c2.escrever("Ola Mundo")
c3.escrever("Ola Mundo")
