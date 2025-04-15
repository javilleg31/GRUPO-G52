//variables globales, los objetos con {}  y los arrays con []
let dicGeneros  = {}
let dicCiudades = {}

modoEditar = false;
idActual = null;


document.getElementById('formulario').addEventListener('submit', async function (e) {
    e.preventDefault(); //Previene que se recarge la página

    //Recolectar los datos del formulario OJO con los ID
    const data = {
        identificacion: identificacion.value,
        nombres: nombres.value,
        fecha: fecha.value,
        genero: genero.value,
        ciudad: ciudad.value,
        movil: movil.value,
        mail: mail.value,
        salario: salario.value
    };

    //DEFINE LA url Y MÉTODO DEPENDIENDO SI EStamos Editando o no 
    const url = modoEditar ? `/persona/${idActual}` : '/persona';
    const metodo = modoEditar ? 'PUT' : 'POST';   //POST para insertar PUT para actualizar

    //enviar la informacion al servidor Flask - await esperar una operación async
    const res = await fetch (url, {
        method: metodo,
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });

    //Muestra el mensaje de exito y actualiza la vista o el formulario
    const json = await res.json();
    alert(json.mensaje || 'Guardado Correctamente');
    limpiar();
    cargar();

});

//Cargar las opciones de los combos
async function cargarOpociones(){
    //llenamos las listas que se encontraban vacias []
    const r1 = await fetch('/generos'); //fetch busca en el app.py @app.route('/generos')
    dicGeneros = await r1.json();       //convertir a formato json
    
    const r2 = await fetch('/ciudades'); //fetch busca en el app.py @app.route('/ciudades')
    dicCiudades = await r2.json();       //convertir a formato json
    
    //carga los selelct 
    //Object.entries convierte el objeto en un array de pares
    //map es un bucle que recorre cada para y construye un string html tipo
    //join juntoar lodos los strin en uno solo sin separadores
    genero.innerHTML = Object.entries(dicGeneros).map (
        ([codigo, nombre]) => `<option value="${codigo}">${nombre}</option>`
    ).join('');
    
    ciudad.innerHTML = Object.entries(dicCiudades).map (
        ([codigo, nombre]) => `<option value="${codigo}">${nombre}</option>`
    ).join('');
    
}

// Carga la tabla al iniciar la página
async function cargar() {
    try {
        const res = await fetch('/personas');      // Espera la respuesta del servidor
        const personas = await res.json();         // Espera convertirla a JSON

        let html = '';
        for (const p of personas) {
            html += `<tr>
                <td>${p[0]}</td>
                <td>${p[1]}</td>
                <td>${p[2]}</td>
                <td>${dicGeneros[p[3]] || p[3]}</td>
                <td>${dicCiudades[p[4]] || p[4]}</td>
                <td>${p[5]}</td>
                <td>${p[6]}</td>
                <td>${p[7]}</td>
                <td>
                    <button class="btn btn-warning btn-sm" onclick='editar(${JSON.stringify(p)})'>Editar</button>
                    <button class="btn btn-danger btn-sm" onclick='eliminar("${p[0]}")'>Eliminar</button>
                </td>
            </tr>`;
        }
        document.getElementById('tabla').innerHTML = html;
    } catch (error) {
        console.error('Error al cargar personas:', error);
    }
}

// Función para llenar el formulario con los datos seleccionados para editar
function editar( p ) {
    modoEditar = true;
    idActual = p[0]; // Guarda el id actual
    identificacion.value = p[0];
    nombres.value = p[1];
    fecha.value = p[2];
    genero.value = p[3];
    ciudad.value = p[4];
    movil.value = p[5];
    mail.value = p[6];
    salario.value = p[7];
    identificacion.disabled = true; // Desactiva el campo ID (clave primaria)
}

// Función para eliminar una persona
function eliminar(id) {
    if (confirm('¿Seguro de eliminar?')) {
        //petición HTTP al backend (Flask).
        //Se está construyendo una URL dinámica: si id es 123, la ruta será /persona/123.
        //DELETE le dice al servidor que queremos eliminar esa persona.
        //La petición quedaria  @app.route('/persona/<identificacion>', methods=['DELETE']).
        fetch(`/persona/${id}`, {method: 'DELETE'})
            .then(r => r.json())     // espera la respuesta y la convierte a JSON
            .then(() => cargar());   // Recarga la tabla después de eliminar
    }
}

// Función para limpiar el formulario y volver al modo insertar
function limpiar() {
    modoEditar = false;
    idActual = null;
    formulario.reset(); // Limpia el formulario
    identificacion.disabled = false; // Habilita nuevamente el ID
}

// Función para filtrar la tabla según el texto que se escribe en el input buscar
function filtrarTabla() {
    const filtro = buscar.value.toLowerCase();
    const filas = document.querySelectorAll('#tabla tr');
    filas.forEach(fila => {
        const texto = fila.innerText.toLowerCase();
        fila.style.display = texto.includes(filtro) ? '' : 'none';
    });
}

// Función para exportar la tabla a un archivo Excel (.xls)
function exportarExcel() {
    const tabla = document.querySelector("table").outerHTML;

    const htmlConUTF8 = `
        <html xmlns:o="urn:schemas-microsoft-com:office:office"
              xmlns:x="urn:schemas-microsoft-com:office:excel"
              xmlns="http://www.w3.org/TR/REC-html40">
        <head><meta charset="UTF-8"></head>
        <body>${tabla}</body></html>`;

    // Crea un archivo en memoria (Blob)
    const blob = new Blob([htmlConUTF8], { type: "application/vnd.ms-excel;charset=utf-8;" });

    // Crea un enlace temporal y lo hace clic para descargar
    const enlace = document.createElement("a");  //Simula un clic en un <a> para descargar el archivo.
    enlace.href = URL.createObjectURL(blob);
    enlace.download = "personas_listado.xls";
    enlace.click();
}

//el navegador debe ejecutar automaticamente cuando la página termine de cargar (HTML-CSS-IMAGENER----)
//el await hace que el navegador espere a que termine de ejecutarse esa funion, pero puede ejecutar otras
window.onload = async () => {
    await cargarOpociones() //espera que se llenen las listas desplegables
    cargar()
}
