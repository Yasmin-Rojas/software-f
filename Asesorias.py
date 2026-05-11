class ServicioAsesoria(Servicio):
    def calcular_costo(self):
        return self.costo_base * 1.3

    def descripcion(self):
        return "Asesoría especializada"