class ServicioSala(Servicio):
    def calcular_costo(self):
        return self.costo_base * 1.1

    def descripcion(self):
        return "Reserva de sala"