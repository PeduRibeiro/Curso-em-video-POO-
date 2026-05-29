from abc import ABC, abstractmethod
from random import randint, randrange
from rich import print
from rich.panel import Panel

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca = 1000):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[randrange(0,len(self.golpes))]
            print(f"[green]{self.nome}[/] ({self.vida}) atacou [red]{alvo.nome}[/] ({alvo.vida}) com um [blue]{golpe} de força [/][red]{forca}[/]")
            alvo.receber_dano(forca)
        else:
            print(f"\nO ataque [green]{self.nome} -->[/] {alvo.nome} não pode acontecer \n\n[red on black]RIP --{self.nome} está MORTO--[/]")


    def receber_dano(self, dano):
        fator = randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f"\n[blue]{self.nome}[/] recebeu [red] dano de {fator}[/]! \nVida restante ([magenta]{self.vida}[/])\n")

    @abstractmethod
    def curar(self):
        pass

    def status(self):
        pass

class Guerreira(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Tapa", "Rasgada de unha", "Mordida Super Sonica"]


    def curar(self):
        fator = randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e recuperou [green]{fator} pontos de vida[/]")

class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raio de luz", "Magia Estatica"]


    def curar(self):
        fator = randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] fez uma magia de cura e recuperou [green]{fator} pontos de vida[/]")


