from excepciones.excepciones import ReservaError
from clientes.cliente import Cliente
from servicios.servicios import Servicio

class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if not isinstance(cliente, Cliente):
            raise ReservaError("Cliente inválido")

        if not isinstance(servicio, Servicio):
            raise ReservaError("Servicio inválido")

        if duracion <= 0:
            raise ReservaError("Duración inválida")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "PENDIENTE"

    def confirmar(self):
        self.estado = "CONFIRMADA"

    def cancelar(self):
        self.estado = "CANCELADA"
