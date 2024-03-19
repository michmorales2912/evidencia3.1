class Menu:
    def __init__(self):
        self.items = {
            1: ("Pizza especial", 289),
            2: ("Pizza campesina", 289),
            3: ("Pizza Pancho Villa", 289),
            4: ("Pizza norteña", 320),
            5: ("Pizza chicken-bufalo", 289),
            6: ("Boneless Naturales", 175),
            7: ("Boneless Búfalo", 175),    
            8: ("Boneless Mango-habanero", 175),
            9: ("Boneless BBQ", 175),
            10: ("Spaggetti De la casa", 175),
            11: ("Spaggetti Con crema", 175),
            12: ("Spaggetti Chorizo", 175),
            13: ("Spaggetti Boloñés", 175),
            14: ("Papas fritas Chicas", 110),
            15: ("Papas fritas Grandes", 165),
            16: ("Ensaladas Chicas", 110),
            17: ("Ensaladas Grandes", 165),
            18: ("Agua natural", 28),
            19: ("Coca cola", 28),
            20: ("Fanta", 28),
            21: ("Uva", 28),
            22: ("Fresa", 28),
            23: ("Naranja", 28),
            24: ("Manzanita", 28),
        }

    def agregar_item(self, nombre, precio):
        num_item = max(self.items.keys()) + 1
        self.items[num_item] = (nombre, precio)
        return f"Se ha agregado '{nombre}' al menú con el precio de ${precio}."

    def eliminar_item(self, num_item):
        if num_item in self.items:
            del self.items[num_item]
            return f"Se ha eliminado el ítem número {num_item} del menú."
        else:
            return "El número de ítem proporcionado no existe en el menú."

    def mostrar_menu(self):
        return self.items
