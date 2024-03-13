class Meseros:
    def __init__(self, sistema_pedidos):
        self.sistema_pedidos = sistema_pedidos
        self.ordenes = []
    def añadir(self, numero_orden, elementos):
        if len(self.ordenes) < 6:
            nueva_orden = {'numero_orden': numero_orden, 'elementos': elementos}
            self.ordenes.append(nueva_orden)
            print(f"La orden {numero_orden} fue registrada con éxito.")
        else:
            print("No se pueden aceptar más de 6 órdenes al mismo tiempo.")
   
    def consultar(self):
        try:
            if self.ordenes:
                return self.ordenes[-1]
            else:
                return None
        except Exception as e:
            print(f"Error en el método consultar: {str(e)}")
            return None
        
    def obtener_ultima_orden(self):
        try:
            if self.ordenes:
                return self.ordenes[-1]
            else:
                return None
        except Exception as e:
            print(f"Error en el método obtener_ultima_orden: {str(e)}")
            return None