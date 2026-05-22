from rich import print
from rich import inspect


class Funcionario:
    # Atributos de Classe
    empresa = "Qinttus"

    def __init__(self, nome, setor, cargo):
        # Atributos de Instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentação(self) -> str:
        return f":handshake:Ola! Eu sou [cyan]{self.nome}[/] e atuo no cargo de {self.cargo} no setor {self.setor} da Empresa {self.__class__.empresa}."



f1 = Funcionario('José', 'TI', 'Dev Back End')
print(f1.apresentação())
#inspect(f1)

f2 = Funcionario('Maria', 'TI', 'Dev Front End')
print(f2.apresentação())
#inspect(f2)