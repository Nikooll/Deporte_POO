from persona import Persona

class Jugador(Persona):
    def __init__(self, apellido, nombre, cedula, sexo, categoria, foto):
        super().__init__(apellido, nombre, cedula, sexo)
        self.categoria = categoria
        self.foto = foto
