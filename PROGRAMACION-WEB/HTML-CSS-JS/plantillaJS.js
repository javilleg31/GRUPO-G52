//variables globales
const PI = 3.1416

// Espera a que cargue el DOM Document Object Model → Modelo de Objetos del Documento.
window.addEventListener('DOMContentLoaded', () => {
      const form = document.getElementById('formulario');
     
      //addEventListener función de JavaScript que sirve para escuchar eventos en un elemento HTML (Click - submit)
      form.addEventListener('submit', (e) => { //el usuario presiona el boton submit
        e.preventDefault(); // Evita que se recargue
      
        // Captura de datos desde EL FORMULARIO - la mayoría son con .value = 
        const nombre = document.getElementById('nombre').value.trim(); 
        const ciudad = document.getElementById('cboCiudad').value; 
        const futbool = document.getElementById('chkFutbol'); //verificar si chekeado checkbox.checked   
        const genero = document.querySelector('input[name="radGenero"]:checked');
      
        // Validación básica
        if (nombre === '' || ciudad === '' || ! genero || ! !futbool.checked) {
         alert('Por favor, completa todos los campos.');
         return;
        }
      
        // Aquí va tu lógica (guardar, mostrar, enviar, etc.)
        console.log('Datos capturados:', { nombre, ciudad, futbool, genero });
      
        // Resetear formulario - cuando se requiera limpia todos los campos del formulario del submit
        form.reset();
      });
     });