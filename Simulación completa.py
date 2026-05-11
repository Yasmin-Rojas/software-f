from entidades.cliente import Cliente
from entidades.servicios_derivados import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria
)
from entidades.reserva import Reserva

def ejecutar_simulacion():
    operaciones = []

    try:
        # Clientes
        cliente1 = Cliente("Ana", "1010")
        cliente2 = Cliente("Luis", "2020")

        # Servicios
        sala = ServicioSala("Sala VIP", 100)
        equipo = ServicioEquipo("Laptop", 80)
        asesoria = ServicioAsesoria("Consultoría", 120)

        # Reservas válidas
        r1 = Reserva(cliente1, sala, 2)
        r1.confirmar()
        r1.procesar_pago()

        r2 = Reserva(cliente2, equipo, 3)
        r2.confirmar()
        r2.procesar_pago()

        # Reservas con error
        r3 = Reserva(cliente1, asesoria, -1)
        r3.confirmar()

        # Cliente inválido
        try:
            Cliente("", "000")
        except Exception as e:
            print("Error controlado:", e)

        # Más operaciones
        r4 = Reserva(cliente2, sala, 1)
        r4.confirmar()

        r5 = Reserva(cliente1, equipo, 5)
        r5.confirmar()
        r5.cancelar()

        print("Simulación ejecutada correctamente")

    except Exception as e:
        print("Error crítico:", e)

if _name_ == "_main_":
    ejecutar_simulacion()