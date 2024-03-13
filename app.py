from flask import Flask, render_template, request, redirect, session, jsonify
import os
from caja import Caja  
from pedidos import SistemaPedidos  
from meseros import Meseros 
from cocina import Cocina
from menu import Menu



app = Flask(__name__, template_folder='templates', static_folder='static')

app.secret_key = os.urandom(24)
menu_restaurante = Menu()
sistema_pedidos = SistemaPedidos()
meseros_instance = Meseros(SistemaPedidos)


# Index
@app.route('/')
def index():
    return render_template('index.html')

# Caja
@app.route('/caja')
def caja():
    sistema_pedidos = SistemaPedidos()
    caja_instance = Caja(sistema_pedidos)
    return render_template('caja.html', caja_instance=caja_instance)

@app.route('/sumar', methods=['POST'])
def sumar():
    caja_instance = session.get('caja_instance')

    if not caja_instance:
        sistema_pedidos = SistemaPedidos()
        caja_instance = Caja(sistema_pedidos)
        session['caja_instance'] = caja_instance

    mensaje = caja_instance.sumar()
    return jsonify({"message": mensaje})
@app.route('/quitar_elemento', methods=['POST'])
def quitar_elemento():
    caja_instance = session.get('caja_instance')

    if not caja_instance:
        sistema_pedidos = SistemaPedidos()
        caja_instance = Caja(sistema_pedidos)
        session['caja_instance'] = caja_instance
    elemento = request.form.get('elemento')
    mensaje = caja_instance.quitar_elemento(elemento)
    return jsonify({"message": mensaje})

# Meseros
@app.route('/meseros')
def meseros():
    sistema_pedidos = SistemaPedidos()
    meseros_instance = Meseros(sistema_pedidos)
    return render_template('meseros.html', meseros_instance=meseros_instance)

@app.route('/añadir_orden', methods=['POST'])
def añadir_orden():
    try:
        numero_orden = request.form.get('numeroOrden')
        elementos = request.form.get('elementos')
        sistema_pedidos = SistemaPedidos()
        meseros_instance = Meseros(sistema_pedidos)
        meseros_instance.añadir(numero_orden, elementos)

        return jsonify({"message": "Orden añadida correctamente"})
    except Exception as e:
        print(f"Error en añadir_orden: {str(e)}")
        return jsonify({"error": str(e)}), 500
    
@app.route('/consultar_orden', methods=['GET'])
def consultar_orden():
    try:
        ultima_orden = meseros.consultar()
        
        if ultima_orden is not None:
            return jsonify({"message": "Consulta exitosa", "ultima_orden": ultima_orden})
        else:
            return jsonify({"message": "No hay órdenes para consultar"})
    except Exception as e:
        print(f"Error en consultar_orden: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Cocina
@app.route('/cocina')
def cocina():
    sistema_pedidos = SistemaPedidos()
    cocina_instance = Cocina(sistema_pedidos)
    return render_template('cocina.html', cocina_instance=cocina_instance)
@app.route('/consultar_orden_cocina', methods=['GET'])
def consultar_orden_cocina():
    sistema_pedidos = SistemaPedidos()
    cocina_instance = Cocina(sistema_pedidos)
    ultima_orden = cocina_instance.consultar()

    if ultima_orden:
        return jsonify({"numero_orden": ultima_orden['numero_orden'], "elementos": ultima_orden['elementos']})
    else:
        return jsonify({"message": "No hay órdenes en la cocina."})

@app.route('/eliminar_orden_cocina', methods=['POST'])
def eliminar_orden_cocina():
    sistema_pedidos = SistemaPedidos()
    cocina_instance = Cocina(sistema_pedidos)
    cocina_instance.eliminar_orden()

    return jsonify({"message": "Orden eliminada en la cocina."})

#Menu
def obtener_menu():
    menu_restaurante = Menu()
    menu_data = {
        'Pizzas': menu_restaurante.pizzas,
        'Boneless': menu_restaurante.boneless,
        'Spaggetti': menu_restaurante.spaggetti,
        'Papas fritas': menu_restaurante.papas_fritas,
        'Ensaladas': menu_restaurante.ensaladas,
        'Bebidas': menu_restaurante.bebidas,
    }
    return menu_data
@app.route('/menu')
def mostrar_menu():
    menu = {
        "Pizzas": menu_restaurante.pizzas,
        "Boneless": menu_restaurante.boneless,
        "Spaggetti": menu_restaurante.spaggetti,
        "Papas fritas": menu_restaurante.papas_fritas,
        "Ensaladas": menu_restaurante.ensaladas,
        "Bebidas": menu_restaurante.bebidas
    }

    return render_template('menu.html', menu=menu)
if __name__ == '__main__':
    app.run(debug=True)
