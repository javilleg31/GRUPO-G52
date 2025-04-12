function calcular( operacion ){
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
                  }
                  else {
                    mensajeResultado = "DIVISION";
                    resultado = "NO DIVIDIR POR CERO";
                  }
                  break;
        default:  resultado = "OPERACION DESCONOCIDA"; break;
    }
    document.getElementById("txtResultado").value = resultado;
    document.getElementById("lblResultado").innerHTML = mensajeResultado;
    console.log(resultado)
}
