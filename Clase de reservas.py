class Reserva:
    def _init_(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            if self.duracion <= 0:
                raise ValueError("Duración inválida")
            self.estado = "Confirmada"
        except Exception as e:
            self.registrar_error(e)

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar_pago(self):
        try:
            costo = self.servicio.calcular_costo() * self.duracion
            return costo
        except Exception as e:
            self.registrar_error(e)

    def registrar_error(self, error):
        with open("logs.txt", "a") as archivo:
            archivo.write(f"Error: {str(error)}\n")