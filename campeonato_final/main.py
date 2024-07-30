from equipo import Equipo
from registro_encuentro import RegistroEncuentro
from campeonato import Campeonato
from sistema_puntacion import SistemaPuntacion
from tabla_posiciones import TablaPosiciones


def main():
    # Crear equipos
    equipo1 = Equipo("Barrio1", "Rojo", True, "Equipo1")
    equipo2 = Equipo("Barrio2", "Azul", True, "Equipo2")
    equipo3 = Equipo("Barrio3", "Verde", True, "Equipo3")

    # Registrar encuentros
    encuentro1 = RegistroEncuentro("2023-07-29", equipo1, equipo2, 2, 2)
    encuentro2 = RegistroEncuentro("2023-07-30", equipo1, equipo3, 1, 3)

    # Mostrar resultados
    print(
        f"Resultado: {encuentro1.equipo1.nombre_equipo} {encuentro1.puntaje1} - {encuentro1.puntaje2} {encuentro1.equipo2.nombre_equipo}")
    print(
        f"Resultado: {encuentro2.equipo1.nombre_equipo} {encuentro2.puntaje1} - {encuentro2.puntaje2} {encuentro2.equipo2.nombre_equipo}")

    jugadores1 = ["Jugador1", "Jugador2", "Jugador3"]
    jugadores2 = ["Jugador4", "Jugador5", "Jugador6"]
    equipo1.actualizar_jugadores(jugadores1)
    equipo2.actualizar_jugadores(jugadores2)

    campeonato1 = Campeonato(90, "2023-12-01", "2023-07-01", "Mixto", 2, 4, 2, 1)
    campeonato2 = Campeonato(90, "2024-12-01", "2024-07-01", "Mixto", 2, 4, 2, 1)

    # Sistema de puntuación
    sistema_puntacion = SistemaPuntacion(0, 3, 3, 0, 1)
    print("Sistema de puntuación:")
    print(f"  Puntos por victoria: {sistema_puntacion.puntos_por_victoria}")
    print(f"  Puntos por empate: {sistema_puntacion.puntos_por_empate}")

    # Tabla de posiciones
    tabla = TablaPosiciones()
    tabla.actualizar(encuentro1.equipo1, sistema_puntacion.puntos_por_empate)
    tabla.actualizar(encuentro1.equipo2, sistema_puntacion.puntos_por_empate)
    tabla.actualizar(encuentro2.equipo1, sistema_puntacion.puntos_por_perdida)
    tabla.actualizar(encuentro2.equipo2, sistema_puntacion.puntos_por_victoria)

    print("Tabla de posiciones:")
    tabla.mostrar()


if __name__ == "__main__":
    main()
