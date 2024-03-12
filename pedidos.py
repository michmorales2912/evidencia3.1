from collections import deque

class SistemaPedidos:
    def __init__(self):
        self.ordenes = deque(maxlen=6)  

    def verificar_estructura_vacia(self):
        return not bool(self.ordenes)

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

    def eliminar_orden(self):
        if self.ordenes:
            orden_eliminada = self.ordenes.popleft()
            print(f"Se ha eliminado la orden {orden_eliminada['numero_orden']}.")
        else:
            print("No hay órdenes para eliminar.")

    def sumar(self):
        if self.ordenes:
            ultima_orden = self.ordenes[-1]
            print(f"Imprimiendo ticket para la orden {ultima_orden['numero_orden']}.")
        else:
            print("No hay órdenes para imprimir ticket.")

    def quitar_elemento(self, elemento):
        if self.ordenes:
            ultima_orden = self.ordenes[-1]
            if elemento in ultima_orden['elementos']:
                ultima_orden['elementos'].remove(elemento)
                print(f"Se ha quitado el elemento {elemento} de la orden {ultima_orden['numero_orden']}.")
            else:
                print(f"El elemento {elemento} no está en la orden.")
        else:
            print("No hay órdenes para quitar elementos.")


