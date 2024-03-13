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
    console.log("Datos a enviar: ", numeroOrden, elementos)
    fetch('/añadir_orden', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'numeroOrden=' + encodeURIComponent(numeroOrden) + '&elementos=' + encodeURIComponent(elementos),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);  
    });
}


function consultarOrden() {
    fetch('/consultar_orden')
        .then(response => response.json())
        .then(data => {
            var resultadoConsulta = document.getElementById("resultadoConsulta");

            if (data.numero_orden) {
                resultadoConsulta.innerHTML = "Última Orden: Número " + data.numero_orden + ", Elementos: " + data.elementos;
            } else {
                resultadoConsulta.innerHTML = "No hay órdenes para consultar.";
            }
        })
        .catch(error => {
            console.error('Error al consultar la orden:', error);
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