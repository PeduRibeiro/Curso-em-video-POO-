from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    def frete(self):
        pass

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return f"RS{self.frete:.2f}"


class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        self.frete = self.distancia * Caminhao.fator
        if self.distancia >= 50:
            return f"RS{self.frete:.2f}"
        else:
            return f"Faltaram {50 - self.distancia:.2f}Km para dist minima"

class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia <= 10:
            return f"{self.distancia * 9.50}"
        else:
            return f"ultrapassaram {self.distancia - 10:.2f}Km da dist maxima"
