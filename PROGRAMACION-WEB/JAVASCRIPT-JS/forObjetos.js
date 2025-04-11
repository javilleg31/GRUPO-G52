// Bucle for...in  para recorrer  Objetos
const objeto = { a: 1, b: 2, c: 3 };  //similar a diccionarios en python con clave: valor

for (let key in objeto) {
    console.log(`for...in: ${key} = ${objeto[key]}`);
}
