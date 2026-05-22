from rich import print
import time
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: :arrow_forward: [blue]Você acabou de abrir o livro [red]'{self.titulo}'[/] que tem [green]{self.total_paginas} paginas[/] no total. \nVocê está na[/] [yellow]pagina {self.pagina_atual}[/]")

    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pag{self.pagina_atual} :arrow_forward: ", end='')
                time.sleep(0.2)
                cont += 1
        print(f"\n[blue]Você avançou {cont} paginas e agora está na[/] [yellow]pagina {self.pagina_atual}[/]")
        if self.fim_do_livro():
            print(f":closed_book: :arrow_forward: [red] Você chegou ao fim do livro '{self.titulo}'[/]")

    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False

        p

l1 = Livro("Metamorfose", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)
l1.avancar_paginas(5)