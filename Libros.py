class Libros:
    def __init__(self, titulo, autor, total_paginas):
        
        self.__titulo = titulo
        self.__autor = autor
        self.__total_paginas = total_paginas
        self.__pagina_actual = 1 

    
    def avanzar_paginas(self, paginas):
        nueva_pagina = self.__pagina_actual + paginas
        if nueva_pagina <= self.__total_paginas:
            self.__pagina_actual = nueva_pagina
            print(f"Avanzaste {paginas} páginas. Ahora estás en la {self.__pagina_actual}.")
        else:
            
            raise ValueError(f"Error: No puedes avanzar a la página {nueva_pagina}. El libro solo tiene {self.__total_paginas} páginas.")

    
    def retroceder_paginas(self, paginas):
        nueva_pagina = self.__pagina_actual - paginas
        if nueva_pagina >= 1:
            self.__pagina_actual = nueva_pagina
            print(f"Retrocediste {paginas} páginas. Ahora estás en la {self.__pagina_actual}.")
        else:
            
            raise ValueError("Error: No puedes retroceder antes de la página 1.")

    
    def consultar_pagina_actual(self):
        return self.__pagina_actual

    def obtener_informacion(self):
        return {
            "Título": self.__titulo,
            "Autor": self.__autor,
            "Total": self.__total_paginas,
            "Página Actual": self.__pagina_actual
        }


mi_libro = Libros("Las mujeres que aman demasiado", "Robin Norwood", 336)
print(f"Iniciando lectura de: {mi_libro.obtener_informacion()['Título']}")

mi_libro.avanzar_paginas(50)
mi_libro.retroceder_paginas(10)

print(f"Estado actual: {mi_libro.obtener_informacion()}")
