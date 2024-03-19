from collections import deque
from Menu import Menu  
class Pedidos:
    def __init__(self, menu):
        self.ordenes = []  
        self.menu = menu  
    
    def añadir(self, item_num, quantity):
        item_info = self.menu.items.get(item_num)
        if item_info:
            item_name, item_price = item_info
            total_price = item_price * quantity  
            self.ordenes[-1].append((item_name, total_price))
            print(f"{quantity} {item_name} fue(ron) agregado(s) a la orden actual.")
        else:
            print("El número de ítem proporcionado no existe en el menú.")

    def crear_nueva_orden(self):
        self.ordenes.append(deque())
        print("Se ha creado una nueva orden.")
    
    def consultar(self):
        return list(self.ordenes)
    
    def eliminar_orden(self, indice):
        if 0 <= indice < len(self.ordenes):
            del self.ordenes[indice]
            print(f"Se ha eliminado la orden número {indice + 1}.")
        else:
            print("El número de orden proporcionado no existe.")
    
    def sumar(self, indice):
        if 0 <= indice < len(self.ordenes):
            print("Imprimiendo ticket de la orden:")
            for item in self.ordenes[indice]:
                print(item)
        else:
            print("El número de orden proporcionado no existe.")

    def quitar_elemento(self, indice):
        if 0 <= indice < len(self.ordenes):
            if self.ordenes[indice]:
                self.ordenes[indice].pop()
                print("Último elemento de la orden eliminado.")
            else:
                print("La orden está vacía.")
        else:
            print("El número de orden proporcionado no existe.")

menu = Menu()
pedidos = Pedidos(menu)
