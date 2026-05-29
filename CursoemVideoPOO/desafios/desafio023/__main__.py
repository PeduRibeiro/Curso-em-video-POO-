from pygments.lexers import q
from rich import print, inspect

from desafios.desafio023.classes import Quadrado, Circulo


def main():
    q = Quadrado(20)
    inspect(q, methods=True)
    print(f"Um quadrado de lado {q.lados}cm tem perimetro de {q.perimetro()}cm")
    print(f"Um quadrado de lado {q.lados}cm tem area de {q.area()}mm tem área de {q.area()}cm²")

    c = Circulo(5)
    inspect(c, methods=True)
    print(f"Um circulo de raio{c.raio}cm tem perimetro de {c.perimetro():.2f}cm")
    print(f"Um circulo de raio{c.raio}cm tem area de {c.area():.2f}cm²")
if __name__ == '__main__':
    main()