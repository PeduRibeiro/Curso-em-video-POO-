from personagem import *
from rich import inspect

def main():

    p1 = Guerreira("Taline", 10000)
    p2 = Mago("Paulo", 5000)
    p1.atacar(p2, 1000)
    p1.curar()
    p2.atacar(p1,300)
    p2.curar()

    #inspect(p1, methods=True)
    #inspect(p2,methods= True)

   # p1.receber_dano(10000)
if __name__ == "__main__":
    main()
