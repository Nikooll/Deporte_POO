from equipo import Equipo
from registro_encuentro import RegistroEncuentro
from campeonato import Campeonato
from sistema_puntacion import SistemaPuntacion

def main():
    # Crear equipos
    equipo1 = Equipo("Barrio1", "Rojo", True, "Equipo1")
    equipo2 = Equipo("Barrio2", "Azul", True, "Equipo2")

    # Registrar encuentro
    encuentro = RegistroEncuentro("2023-07-29", equipo1, equipo2, 2, 2)
    
    # Mostrar resultados
    print(f"Resultado: {encuentro.equipo1.nombre_equipo} {encuentro.puntaje1} - {encuentro.puntaje2} {encuentro.equipo2.nombre_equipo}")

    # Crear un campeonato
    campeonato = Campeonato(90, "2023-12-01", "2023-07-01", "Mixto", 2, 4, 2, 1)
    
    # Sistema de puntuación
    sistema_puntacion = SistemaPuntacion(0, 3, 3, 0, 1)
    print("Sistema de puntuación:")
    print(f"  Puntos por victoria: {sistema_puntacion.puntos_por_victoria}")
    print(f"  Puntos por empate: {sistema_puntacion.puntos_por_empate}")

if __name__ == "__main__":
    main()
