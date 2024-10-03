class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo
        self.ciudad = ciudad  # Atributo

    def saludar(self):
        """Método para saludar a la persona."""
        print(f"Hola, mi nombre es {self.nombre}.")

    def saludo(self):
        """Método para saludar a otra persona."""
        print(f"{self.nombre} mando a saludar a {self.nombre}.")

    def cumplir_anios(self):
        """Método para incrementar la edad de la persona en un año."""
        self.edad += 1
        print(f"Ahora tengo {self.edad} años.")

    def mover(self, nueva_ciudad):
        """Método para cambiar la ciudad de la persona."""
        self.ciudad = nueva_ciudad
        print(f"Me he mudado a {self.ciudad}.")

    def describir(self):
        """Método para describir a la persona."""
        print(f"Soy {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}.")

    def es_mayor_de_edad(self):
        """Método para verificar si la persona es mayor de edad."""
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")

# Crear una instancia de la clase Persona
persona1 = Persona("Carlos", 25, "Madrid")
persona2 = Persona("Juan", 19, "Mexico")
persona3 = Persona("Victor", 10, "Mexico")
persona4 = Persona("Brenda", 21, "Mexico")

# Llamar a los métodos de la instancia
persona1.saludar() # Salida: Hola, mi nombre es Carlos.
persona1.saludo()
persona1.describir()               # Salida: Soy Carlos, tengo 25 años y vivo en Madrid.
persona1.cumplir_anios()          # Salida: Ahora tengo 26 años.
persona1.mover("Barcelona")       # Salida: Me he mudado a Barcelona.
persona1.describir()               # Salida: Soy Carlos, tengo 26 años y vivo en Barcelona.
persona1.es_mayor_de_edad()       # Salida: Carlos es mayor de edad.

persona2.saludar()                 # Salida: Hola, mi nombre es Carlos.
persona2.saludo()
persona2.describir()               # Salida: Soy Carlos, tengo 25 años y vivo en Madrid.
persona2.cumplir_anios()          # Salida: Ahora tengo 26 años.
persona2.mover("Pachuca")       # Salida: Me he mudado a Barcelona.
persona2.describir()               # Salida: Soy Carlos, tengo 26 años y vivo en Barcelona.
persona2.es_mayor_de_edad()

persona3.saludar()                 # Salida: Hola, mi nombre es Carlos.
persona3.saludo()
persona3.describir()               # Salida: Soy Carlos, tengo 25 años y vivo en Madrid.
persona3.cumplir_anios()          # Salida: Ahora tengo 26 años.
persona3.mover("Quintana Roo")       # Salida: Me he mudado a Barcelona.
persona3.describir()               # Salida: Soy Carlos, tengo 26 años y vivo en Barcelona.
persona3.es_mayor_de_edad()

persona4.saludar()                 # Salida: Hola, mi nombre es Carlos.
persona4.saludo()
persona4.describir()               # Salida: Soy Carlos, tengo 25 años y vivo en Madrid.
persona4.cumplir_anios()          # Salida: Ahora tengo 26 años.
persona4.mover("Queretaro")       # Salida: Me he mudado a Barcelona.
persona4.describir()               # Salida: Soy Carlos, tengo 26 años y vivo en Barcelona.
persona4.es_mayor_de_edad()
