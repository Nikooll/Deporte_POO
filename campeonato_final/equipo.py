class Equipo:
    def __init__(self, barrio, color_uniforme, genero, nombre_equipo, jugadores=None):
        self.barrio = barrio
        self.color_uniforme = color_uniforme
        self.genero = genero
        self.nombre_equipo = nombre_equipo
        self.jugadores = jugadores if jugadores else []

    def actualizar_jugadores(self, nuevos_jugadores):
        self.jugadores = nuevos_jugadores
