from rich import print
from rich.panel import Panel

class Churrasco:
        # Atributos de classe
        consumo_padrão = 0.400 # Cada pessoa come em media 400g de carne
        preco_kg = 85.00 # Cada Kg de carne custa 85.00

        def __init__(self, titulo, quant):
            self.titulo = titulo
            self.participantes = quant

        def __str__(self):
            return f"Esse é {self.titulo} com {self.participantes} participantes"

        def calcular_qnt_carne(self) -> float:
            return self.participantes * Churrasco.consumo_padrão

        def calcular_custo_total(self) -> float:
            return self.calcular_qnt_carne() * self.__class__.preco_kg

        def calcular_custo_individual(self) -> float:
            return self.calcular_custo_total() / self.participantes

        def analisar(self):
            conteudo = f"Analisando [cyan]{self.titulo}[/] com [purple]{self.participantes} participantes[/]"
            conteudo += f"\nCada participante comerá [red]{Churrasco.consumo_padrão} Kg de carne[/] e cada [green]KG de carne custa R${Churrasco.preco_kg:,.2f}[/]"
            conteudo += f"\nRecomendo [blue]comprar {self.calcular_qnt_carne():.3f}Kg[/] de carne"
            conteudo += f"\nCada pessoa pagará [yellow]R${self.calcular_custo_individual():,.2f}[/] para participar"
            painel = Panel(conteudo, title=self.titulo)
            conteudo = "..."
            print(painel)

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()


c2 = Churrasco("Festa fim de ano", 80)
c2.analisar()