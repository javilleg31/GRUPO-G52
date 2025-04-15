//variables globales// 
//Espera a que cargue el DOM Document Object Model → Modelo de Objetos del Documento.
window.addEventListener('DOMContentLoaded', () => {
      const formulario = document.getElementById('formulario');
     
      //addEventListener función de JavaScript que sirve para escuchar eventos en un elemento HTML (Click - submit)
      formulario.addEventListener('submit', (e) => { //el usuario presiona el boton submit
        e.preventDefault(); // Evita que se recargue

  });
 });
    

function calcular( operacion ) {
    //extraer los valores de las cajas de texto
    let numero1 = parseFloat(document.getElementById("txtNumero1").value);
    let numero2 = parseFloat(document.getElementById("txtNumero2").value);
    let resultado = 0;
    let mensajeResultado = "Resultado";
    switch (operacion){
        case '+': resultado = numero1 + numero2; mensajeResultado = "SUMO"; break;
        case '-': resultado = numero1 - numero2; mensajeResultado = "RESTO"; break;
        case '*': resultado = numero1 * numero2; mensajeResultado = "MULTIPLICO"; break;
        case '/': if (numero2 != 0) {
                     resultado = numero1 / numero2; 
                     mensajeResultado = "DIVIDIO"; 
                     break;
                  }
                  else {
                    mensajeResultado = "DIVISION";
                    resultado = "NO DIVIDIR POR CERO";
                    break;
                  }
                  
        default:  resultado = "OPERACION DESCONOCIDA"; break;
    }
    document.getElementById("txtResultado").value = resultado;
    document.getElementById("lblResultado").innerHTML = mensajeResultado;
    console.log(resultado)

}
