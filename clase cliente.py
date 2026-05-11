class Cliente(EntidadBase):
    def _init_(self, nombre, identificacion):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if not identificacion:
            raise ValueError("La identificación es obligatoria")
        
        self.__nombre = nombre
        self.__identificacion = identificacion

    def mostrar_info(self):
        return f"Cliente: {self._nombre}, ID: {self._identificacion}"