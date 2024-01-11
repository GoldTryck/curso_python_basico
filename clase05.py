
class Persona:

    def __init__(self, nombre: str, apellido: str, edad: int):
        self.nombre = nombre
        self.apellido = apellido
        self.__edad = edad

    def get_edad(self):
        return self.__edad

    def descripcion(self):
        return print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.get_edad()} años\n")

    def saludar(self):
        return print(f"Hola, soy {self.nombre}\n")


class Estudiante(Persona):
    def __init__(self, nombre: str, apellido: str, edad: int, semestre: int):
        super().__init__(nombre, apellido, edad)
        self.semestre = semestre

    def saludar(self):
        return print(f"Qué tal, soy estudiante y tengo {self.get_edad()} años\n")


class Profesionista(Persona):
    def __init__(self, nombre: str, apellido: str, edad: int, profesion: str):
        super().__init__(nombre, apellido, edad)
        self.profesion = profesion

    def saludar(self):
        return print(f"Mucho gusto, yo soy {self.profesion}")


persona_1 = Persona('Juan', 'Perez', 20)
estudiante_1 = Estudiante('David', 'Ramos', 19, 6)
profesionista_1 = Profesionista('Rodrigo', 'Aguilar', 30, 'Ing. Computacion')


def obtener_saludo(persona):
    persona.saludar()


obtener_saludo(persona_1)
obtener_saludo(estudiante_1)
obtener_saludo(profesionista_1)
