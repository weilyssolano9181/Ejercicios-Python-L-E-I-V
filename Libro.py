class Libro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_info(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Número de páginas:", self.paginas)

    def actualizar_paginas(self, nuevas_paginas):
        self.paginas = nuevas_paginas
        print("El número de páginas fue actualizado.")


libro1 = Libro("Querida yo, debemos hablar", "Elizabeth Clapés", 320)

libro1.mostrar_info()

libro1.actualizar_paginas(330)

libro1.mostrar_info()