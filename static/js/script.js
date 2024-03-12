//Index
function mostrarMenu(area) {
    alert(`Has seleccionado ${area}`);
}

//Caja
function sumar() {

    $.ajax({
        type: "POST",
        url: "/sumar",  
        success: function (response) {
            alert(response);
        },
        error: function (error) {
            alert("Error al imprimir ticket.");
        }
    });
}

function quitarElemento() {
    var elemento = document.getElementById("elemento").value;

    $.ajax({
        type: "POST",
        url: "/quitar_elemento",  
        data: { elemento: elemento },
        success: function (response) {
            alert(response);
        },
        error: function (error) {
            alert("Error al quitar elemento.");
        }
    });
}

//Meseros
function añadirOrden() {
    var numeroOrden = document.getElementById("numeroOrden").value;
    var elementos = document.getElementById("elementos").value;

    $.ajax({
        type: "POST",
        url: "/añadir_orden",  
        data: { numeroOrden: numeroOrden, elementos: elementos },
        success: function (response) {
            alert(response.message);
        },
        error: function (error) {
            alert("Error al añadir orden.");
        }
    });
}

function consultarOrden() {
    $.ajax({
        type: "GET",
        url: "/consultar_orden",  
        success: function (response) {
            if (response) {
                alert("Última orden consultada: " + JSON.stringify(response));
            } else {
                alert("No hay órdenes para consultar.");
            }
        },
        error: function (error) {
            alert("Error al consultar orden.");
        }
    });
}

//Cocina
function consultarOrdenCocina() {
  
    $.ajax({
        type: "GET",
        url: "/consultar_orden_cocina",  
        success: function (response) {
            if (response) {
                alert("Última orden en cocina: " + JSON.stringify(response));
            } else {
                alert("No hay órdenes en la cocina.");
            }
        },
        error: function (error) {
            alert("Error al consultar orden en cocina.");
        }
    });
}

function eliminarOrdenCocina() {
    $.ajax({
        type: "POST",
        url: "/eliminar_orden_cocina", 
        success: function (response) {
            alert(response.message);
        },
        error: function (error) {
            alert("Error al eliminar orden en cocina.");
        }
    });
}