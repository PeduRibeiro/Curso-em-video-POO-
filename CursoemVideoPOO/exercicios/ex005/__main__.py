from rich import print, inspect
from classesex005 import Aluno, Professor, Funcionario

def main():
    a1 = Aluno("Vitor", 19, "Informatica", "T01")
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor("Samuel", 35, "Biologia", "Mestrado")
    p1.dar_aula()

    f1 = Funcionario("Claudia", 30, "Secretaria", "Secretaria")
    f1.fazer_aniversario()
    f1.bater_ponto()

    #inspect(p1, methods=True)
    #inspect(a1, methods=True)
    #inspect(f1, methods=True)

if __name__ == '__main__':
    main()
