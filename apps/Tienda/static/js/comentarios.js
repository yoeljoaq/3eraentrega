// Cargar los comentarios guardados en el almacenamiento local al cargar la página
window.addEventListener('load', function() {
  cargarComentariosGuardados();
});

// Función para cargar los comentarios guardados en el almacenamiento local
function cargarComentariosGuardados() {
  var comentarios = localStorage.getItem('comentarios');
  if (comentarios) {
    comentarios = JSON.parse(comentarios);
    comentarios.forEach(function(comentario) {
      agregarTarjeta(comentario.nombre, comentario.mensaje, comentario.valoracion, comentario.id);
    });
  }
}

// Función para guardar los comentarios en el almacenamiento local
function guardarComentario(nombre, mensaje, valoracion, id) {
  var comentarios = localStorage.getItem('comentarios');
  if (comentarios) {
    comentarios = JSON.parse(comentarios);
  } else {
    comentarios = [];
  }
  comentarios.push({ nombre: nombre, mensaje: mensaje, valoracion: valoracion, id: id });
  localStorage.setItem('comentarios', JSON.stringify(comentarios));
}

// Función para eliminar un comentario del almacenamiento local
function eliminarComentario(id) {
  var comentarios = localStorage.getItem('comentarios');
  if (comentarios) {
    comentarios = JSON.parse(comentarios);
    comentarios = comentarios.filter(function(comentario) {
      return comentario.id !== id;
    });
    localStorage.setItem('comentarios', JSON.stringify(comentarios));
  }
}

// Función para agregar una nueva tarjeta de comentario
function agregarTarjeta(nombre, mensaje, valoracion, id) {
  var contenedor = document.getElementById('comentarios');
  var tarjeta = document.createElement('div');
  tarjeta.className = 'tarjeta';
  tarjeta.innerHTML = '<strong>' + nombre + '</strong><br>' +
                      mensaje + '<br>' +
                      'Valoración: ' + valoracion + ' estrellas' +
                      '<button class="eliminar" data-id="' + id + '">Eliminar</button>';
  contenedor.appendChild(tarjeta);
}

// Manejador de eventos para enviar comentarios
document.getElementById('formulario').addEventListener('submit', function(e) {
  e.preventDefault();
  var nombre = document.getElementById('nombre').value;
  var mensaje = document.getElementById('mensaje').value;
  var valoracion = document.querySelector('input[name="rating"]:checked').value;
  var id = Date.now().toString(); // Generar un ID único utilizando la marca de tiempo
  agregarTarjeta(nombre, mensaje, valoracion, id);
  guardarComentario(nombre, mensaje, valoracion, id);
  document.getElementById('formulario').reset();
});

// Manejador de eventos para eliminar comentarios
document.getElementById('comentarios').addEventListener('click', function(e) {
  if (e.target.classList.contains('eliminar')) {
    var id = e.target.getAttribute('data-id');
    e.target.parentNode.remove();
    eliminarComentario(id);
  }
});
