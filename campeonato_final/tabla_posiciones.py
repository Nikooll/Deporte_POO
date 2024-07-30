class TablaPosiciones:
    def __init__(self):
        self.posiciones = {}

    def actualizar(self, equipo, puntos):
        if equipo.nombre_equipo not in self.posiciones:
            self.posiciones[equipo.nombre_equipo] = 0
        self.posiciones[equipo.nombre_equipo] += puntos

    def mostrar(self):
        for equipo, puntos in sorted(self.posiciones.items(), key=lambda item: item[1], reverse=True):
            print(f"{equipo}: {puntos} puntos")
