#persona y cliente

from abc import ABC
from excepciones.excepciones import ClienteError

class Persona(ABC):

    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento


class Cliente(Persona):

    def __init__(self, nombre, documento, correo):

        super().__init__(nombre, documento)

        if not nombre.strip():
            raise ClienteError("Nombre vacío")

        if len(documento) < 5:
            raise ClienteError("Documento inválido")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        self.__correo = correo

    def mostrar_info(self):
        return f"{self.nombre} | {self.documento} | {self.__correo}"
