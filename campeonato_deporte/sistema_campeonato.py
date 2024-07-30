from abc import ABC, abstractmethod

class SistemaCampeonato(ABC):
    @abstractmethod
    def jugar_partido(self):
        pass

    @abstractmethod
    def calcular_resultados(self):
        pass
