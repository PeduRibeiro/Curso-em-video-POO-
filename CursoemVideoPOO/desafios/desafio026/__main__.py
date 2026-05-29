from funcionario import *


def main():

    f1 = FuncionarioHorista("Vitor Bi", 45)
    f1.calc_salario()
    f1.analisar_salario()
    #inspect(f1)

    f2 = FuncionarioMensalista("Taline Fatima", 5_900)
    f2.calc_salario()
    f2.analisar_salario()

if __name__ == "__main__":
    main()
