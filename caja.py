class Caja:
    def __init__(self, sistema_pedidos):
        self.sistema_pedidos = sistema_pedidos

    def sumar(self):
        if self.sistema_pedidos.ordenes:
            ultima_orden = self.sistema_pedidos.ordenes[-1]
            print(f"Imprimiendo ticket para la orden {ultima_orden['numero_orden']}.")
        else:
            print("No hay órdenes para imprimir ticket.")

    def quitar_elemento(self, elemento):
        if self.sistema_pedidos.ordenes:
            ultima_orden = self.sistema_pedidos.ordenes[-1]
            if elemento in ultima_orden['elementos']:
                ultima_orden['elementos'].remove(elemento)
                print(f"Se ha quitado el elemento {elemento} de la orden {ultima_orden['numero_orden']}.")
            else:
                print(f"El elemento {elemento} no está en la orden.")
        else:
            print("No hay órdenes para quitar elementos.")