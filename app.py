from flask import Flask, render_template, request, redirect
from Menu import Menu
from Pedidos import Pedidos

app = Flask(__name__, static_url_path='/static')
menu_instance = Menu()  
pedidos_instance = Pedidos(menu_instance) 

@app.route('/')
def index():
    return render_template('index.html')

# Cajas

@app.route('/Cajas')
def cajas():
    return render_template('Cajas.html')

@app.route('/Sumar', methods=['GET', 'POST'])
def sumar():
    if request.method == 'POST':
        print("Form submitted!")  
        index_pedido = int(request.form['pedido'])
        order = pedidos_instance.ordenes[index_pedido]
        total_pedido = sum(item[1] for item in order)
        return render_template('Sumar.html', pedidos=pedidos_instance.ordenes, total_pedido=total_pedido)
    else:
        return render_template('Sumar.html', pedidos=pedidos_instance.ordenes)




@app.route('/QuitarElementoPedido', methods=['GET', 'POST'])
def quitar_elemento_pedido():
    if request.method == 'POST':
        index_pedido = int(request.form['pedido']) 
        if index_pedido < len(pedidos_instance.ordenes):
            if pedidos_instance.ordenes[index_pedido]:  
                pedidos_instance.ordenes[index_pedido].pop()
        return redirect('/Cajas') 
    else:
        return render_template('QuitarElementoPedido.html', pedidos=pedidos_instance.ordenes)


  

# Meseros

@app.route('/Meseros')
def meseros():
    menu_items = menu_instance.mostrar_menu()  
    return render_template('Meseros.html', menu_items=menu_items)

@app.route('/NuevaOrden', methods=['GET', 'POST'])
def nueva_orden():
    if request.method == 'POST':
        pedidos_instance.crear_nueva_orden()  
        return redirect('/Meseros')
    else:
        return "Invalid request method"

@app.route('/AgregarPedido', methods=['GET', 'POST'])
def agregar_pedido():
    if request.method == 'POST':
        if len(pedidos_instance.ordenes) >=6:
            return "No se pueden agregar más de 6 pedidos a la vez."
        
        item_numbers = request.form.getlist('item_numbers[]')
        item_quantities = request.form.getlist('item_quantities[]')

        if not item_numbers:
            return "No se proporcionaron ítems para agregar a la orden."

        pedidos_instance.crear_nueva_orden()

        for item_number, quantity in zip(item_numbers, item_quantities):
            pedidos_instance.añadir(int(item_number), int(quantity))

        return redirect('/Meseros')
    else:
        menu_items = menu_instance.mostrar_menu()
        return render_template('AgregarPedido.html', menu_items=menu_items)






@app.route('/ConsultarPedidos')
def consultar_pedidos():
    pedidos = pedidos_instance.consultar()
    orders = []
    for pedido in pedidos:
        order = []
        for item in pedido:
            order.append({
                'name': item[0],
                'price': item[1]
            })
        orders.append(order)
    return render_template('ConsultarPedidos.html', orders=orders)




# Cosinas

@app.route('/Cocinas')
def cocinas():
    return render_template('Cocinas.html')


@app.route('/Eliminar')
def eliminar():
    pedidos = pedidos_instance.consultar()
    
    if pedidos:
        primer_pedido = pedidos[0]
        pedidos_instance.eliminar_orden(0)
        mensaje = f"Se eliminó el siguiente pedido: {primer_pedido}"
    else:
        mensaje = "No hay pedidos para eliminar en este momento."
    
    return render_template('Eliminar.html', mensaje=mensaje)


#Menu

@app.route('/Menu')
def menu():
    return render_template('Menu.html')

@app.route('/MenuView')
def view_menu():
    menu_items = menu_instance.mostrar_menu()
    return render_template('MenuView.html', menu_items=menu_items)

@app.route('/AgregarMenu')
def agregar_menu():
    return render_template('AgregarMenu.html')

@app.route('/add_item', methods=['POST'])
def add_item():
    if request.method == 'POST':
        item_name = request.form['item_name']
        item_price = request.form['item_price']
        if item_name and item_price:
            menu_instance.agregar_item(item_name, int(item_price))
    return redirect('/MenuView')

@app.route('/EliminarMenu')
def eiminarmenu():
    return render_template('EliminarMenu.html')

@app.route('/eliminar_item', methods=['POST'])
def eliminar_item():
    if request.method == 'POST':
        item_number = int(request.form['item_number'])
        menu_instance.eliminar_item(item_number)
        return redirect('/EliminarMenu')
    else:
        return "Invalid request method"

if __name__ == '__main__':
    app.run(debug=True)
