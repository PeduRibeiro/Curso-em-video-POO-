from rich import print
from rich.panel import Panel
from rich import  inspect


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick .upper()
        self.favoritos = list()


    def add_favoritor(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f"Nome real: [black on purple] {self.nome} [/]"
        conteudo += f"\nJogos favoritos:"
        for game in enumerate(self.favoritos):
            conteudo += f"\n:video_game:[blue] :arrow_forward: {game[1]}[/]"
        painel = Panel(conteudo, title = f"Jogador <<{self.nick}>>", width = 40)
        print(painel)

j1 = Gamer("paulo ribeiro", "Paulo_pliniow")
j1.add_favoritor("cs")
j1.add_favoritor("fortnite")
j1.add_favoritor("LOL")
j1.add_favoritor("aviator")
j1.ficha()

j2 = Gamer("Taline Carniel", "Taline Raivosa")
j2.add_favoritor("COD")
j2.add_favoritor("LOL")
j2.add_favoritor("aviator")
j2.ficha()


