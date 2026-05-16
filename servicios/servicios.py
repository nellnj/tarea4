

from abc import ABC, abstractmethod
from excepciones.excepciones import ServicioError

class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        if precio_base <= 0:
            raise ServicioError("Precio inválido")

        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, horas=1, impuesto=0):
        return self.precio_base * horas * (1 + impuesto)

    def descripcion(self):
        return "Sala de reuniones"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias=1, descuento=0):
        return self.precio_base * dias * (1 - descuento)

    def descripcion(self):
        return "Equipo tecnológico"


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, sesiones=1, impuesto=0.19):
        return self.precio_base * sesiones * (1 + impuesto)

    def descripcion(self):
        return "Asesoría profesional"