class Meseros:
    def __init__(self, sistema_pedidos):
        self.sistema_pedidos = sistema_pedidos
    def añadir(self, numero_orden, elementos):
        if len(self.ordenes) < 6:
            self.ordenes.append({'numero_orden': numero_orden, 'elementos': elementos})
            print(f"La orden {numero_orden} fue registrada con éxito.")
        else:
            print("No se pueden aceptar más de 6 órdenes al mismo tiempo.")

    def consultar(self):
        if self.ordenes:
            return self.ordenes[-1]
        else:
            return None