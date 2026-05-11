class ServicioEquipo(Servicio):
    def calcular_costo(self):
        return self.costo_base * 1.2

    def descripcion(self):
        return "Alquiler de equipo"