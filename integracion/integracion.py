from cliente.cliente import Cliente
from servicios.servicios import *
from reserva.reserva import Reserva
from excepciones.excepciones import *
import logging

clientes = []
servicios = []
reserva = []

print("\n SOFTWARE FJ\n")


operaciones = [

    lambda: clientes.append(Cliente("Carlos", "12345", "carlos@gmail.com")),

    lambda: clientes.append(Cliente("", "22", "error")),  # error

    lambda: servicios.append(ReservaSala("Sala", 100)),

    lambda: servicios.append(AlquilerEquipo("Laptop", 80)),

    lambda: servicios.append(AsesoriaEspecializada("IA", 150)),

    lambda: reserva.append(Reserva(clientes[0], servicios[0], 2)),

    lambda: reserva[0].confirmar(),
]


for i, op in enumerate(operaciones, 1):

    print(f"Operación {i}")

    try:
        op()

    except Exception as e:
        print("Error:", e)
        logging.error(str(e))

print("\nSistema finalizado")