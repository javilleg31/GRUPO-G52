
//dada una nota indicar aprobado, reprobado o habilita

let nota = 5

let mensaje = "NO RECONOZCO LA NOTA";

if (nota >= 3){
    mensaje = "APRUEBA";
}
else if (nota < 2){
    mensaje = "REPRUEBA"
}
else {
    mensaje = "HABILITA"
}

console.log(`${nota} ${mensaje}`)

