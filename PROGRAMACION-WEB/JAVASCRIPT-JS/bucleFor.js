
//escribir los primeros N multiplos de 5, cuanto suman al final
const N = 10
let multipo = 5;
let multiploInicial = 5;
let suma = 0
//  1. varib control inicia en un valor   2. var control vs vlr final  3. var incremetada
/*for (let contador = 1;                    contador <= N;                 contador++){
    multipo = multipo * contador
    //console.log(multipo * contador);
    console.log(multipo)
    suma = suma + multipo;
}*/

//console.log(`SUMATORIA DE LOS ${N} MULTIPOS de ${multiploInicial} = ${suma} `)

//otra forma
for (let contador = multipo; contador <= N * multipo; contador+=5){
    console.log(contador);
}