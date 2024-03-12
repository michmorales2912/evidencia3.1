#Menu
class Menu:
    def __init__(self):
        self.pizzas = [
            {"id": 1, "nombre": "Pizza especial", "precio": 289},
            {"id": 2, "nombre": "Pizza campesina", "precio": 289},
            {"id": 3, "nombre": "Pizza Pancho Villa", "precio": 289},
            {"id": 4, "nombre": "Pizza norteña", "precio": 320},
            {"id": 5, "nombre": "Pizza chicken-bufalo", "precio": 289}
        ]

        self.boneless = [
            {"id": 11, "nombre": "Naturales", "precio": 175},
            {"id": 12, "nombre": "Búfalo", "precio": 175},
            {"id": 13, "nombre": "Mango-habanero", "precio": 175},
            {"id": 14, "nombre": "BBQ", "precio": 175}
        ]

        self.spaggetti = [
            {"id": 6, "nombre": "De la casa", "precio": 175},
            {"id": 7, "nombre": "Con crema", "precio": 175},
            {"id": 8, "nombre": "Chorizo", "precio": 175},
            {"id": 9, "nombre": "Boloñés", "precio": 175}
        ]

        self.papas_fritas = [
            {"id": 15, "nombre": "Chicas", "precio": 110},
            {"id": 16, "nombre": "Grandes", "precio": 165}
        ]

        self.ensaladas = [
            {"id": 17, "nombre": "Chicas", "precio": 110},
            {"id": 18, "nombre": "Grandes", "precio": 165}
        ]

        self.bebidas = [
            {"id": 19, "nombre": "Agua natural", "precio": 28},
            {"id": 21, "nombre": "Coca cola", "precio": 28},
            {"id": 22, "nombre": "Fanta", "precio": 28},
            {"id": 23, "nombre": "Uva", "precio": 28},
            {"id": 24, "nombre": "Fresa", "precio": 28},
            {"id": 25, "nombre": "Naranja", "precio": 28},
            {"id": 26, "nombre": "Manzanita", "precio": 28}
        ]

    def mostrar_menu(self):
        print("----------- Menú -----------")
        self.mostrar_categoria("Pizzas", self.pizzas)
        self.mostrar_categoria("Boneless", self.boneless)
        self.mostrar_categoria("Spaggetti", self.spaggetti)
        self.mostrar_categoria("Papas fritas", self.papas_fritas)
        self.mostrar_categoria("Ensaladas", self.ensaladas)
        self.mostrar_categoria("Bebidas", self.bebidas)

    def mostrar_categoria(self, nombre_categoria, lista_items):
        print(f"\n{nombre_categoria}")
        for item in lista_items:
            print(f"{item['id']} {item['nombre']} ${item['precio']}")

menu_restaurante = Menu()
menu_restaurante.mostrar_menu()