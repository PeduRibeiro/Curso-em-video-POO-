from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 8
    vol_min: int = 1
    vol_max: int = 6

    def __init__(self, canal = 1, volume = 1):
        self.canal_atual:int = canal
        self.vol_atual:int = volume
        self.ligado:bool = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def vol_mais(self):
        if self.ligado:
            if self.vol_atual != ControleRemoto.canal_max:
                self.vol_atual += 1

    def vol_menos(self):
        if self.ligado:
            if self.vol_atual != ControleRemoto.canal_min:
                self.vol_atual -= 1

    def mostrar_tv(self):

        conteudo = ''
        if not self.ligado:
            conteudo = f"\n\n\n:prohibited: [red on black] A TV está desligada \n\n\n[/]"
        else:
            conteudo = F"\n\nCANAL = "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += (f"[yellow on black] {canal} [/]")
                else:
                    conteudo += f" {canal}"
            conteudo += f"\n\n\nVOLUME ="
            for volume in range(ControleRemoto.vol_min, ControleRemoto.vol_max + 1):
                if volume <= self.vol_atual:
                    conteudo += "[black on cyan]   [/]"
                else:
                    conteudo += f"[black on white]   [/]"

        tv = Panel (conteudo, title="[purple on black]  [  TV  ]  [/]", width=30)
        print(tv)


c = ControleRemoto()
while True:
    c.mostrar_tv()
    comando = str(input(f" < CH{c.canal_atual} > - VOL{c.vol_atual} > + "))
    match comando:
        case '0':
            break
        case '@':
            c.liga_desliga()
        case '>':
            c.canal_mais()
        case '<':
            c.canal_menos()
        case '-':
            c.vol_menos()
        case '+':
            c.vol_mais()
    print("\n" * 10)
