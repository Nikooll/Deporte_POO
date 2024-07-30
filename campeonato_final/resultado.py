from equipo import Equipo

class Resultado:
    def __init__(self, equipo1, equipo2, puntaje1, puntaje2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.puntaje1 = puntaje1
        self.puntaje2 = puntaje2

    def obtener_ganador(self):
        if self.puntaje1 > self.puntaje2:
            return self.equipo1
        elif self.puntaje1 < self.puntaje2:
            return self.equipo2
        else:
            return None
