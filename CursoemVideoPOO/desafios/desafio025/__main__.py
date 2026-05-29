from Transportes import *
from rich import print, inspect
from rich.table import Table


def main():
    dist = 40

    viagem = [ Moto(dist), Caminhao(dist), Drone(dist)]

    #entrega = Caminhao(dist)
    #print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}")

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distancia", justify="center")
    tabela.add_column("Tipo", justify="center")
    tabela.add_column("Frete", justify="center")

    for item in viagem:
        tabela.add_row(f"{dist}Km", f"{type(item).__name__}", f"{item.calc_frete()}")

    print(tabela)




if "__main__" == __name__:
    main()
