from cafeteria import *

def main():
    b1 = Cafe()
    b2 = Leite()
    b3 = Cha()

    b1.preparar()
    b2.preparar()
    b3.preparar()

if "__main__" == __name__:
    main()