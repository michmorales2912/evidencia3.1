from collections import deque
class Cocina:
    def __init__(self, sistema_pedidos):
        self.sistema_pedidos = sistema_pedidos
        self.ordenes = deque(maxlen=6)
    def consultar(self):
        if self.ordenes:
            return self.ordenes[-1]
        else:
            return None
        
    def eliminar_orden(self):
        if self.ordenes:
            orden_eliminada = self.ordenes.popleft()
            print(f"Se ha eliminado la orden {orden_eliminada['numero_orden']}.")
        else:
            print("No hay órdenes para eliminar.")
