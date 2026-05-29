from abc import ABC, abstractmethod


class BebidaQuente(ABC):

    def preparar(self):
        print ("\n----Iniciando o Preparo----")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("---Bebida Pronta---\n")

    def ferver_agua(self):
        print("1° Fervendo agua a 100° Celcius.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        print("2° Passando agua pressurizada pelo café moído.")

    def servir(self):
        print("3. Servindo em xicara pequena")


class Cha(BebidaQuente):
    def misturar(self):
        print("2° Mergulhando o sache de ervas na aguá")

    def servir(self):
        print("3. Servindo em caneca de porcelana com mel e limão")


class Leite(BebidaQuente):
    def misturar(self):
        print("2° Passando vapor pressurizado pelo bico do leite.")

    def servir(self):
        print("3. Servindo na caneca grande com o café")

