

//imprimir los multiplos positivos de N numeros en forma descente
//50  45   40  35   30 ................5
const N = 10
let numero = 5
let resultado = N * numero;
while (resultado > 0){
    console.log(resultado);
    resultado = resultado - numero;
}


