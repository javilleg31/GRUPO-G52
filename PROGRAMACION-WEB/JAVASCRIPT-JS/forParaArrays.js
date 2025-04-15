// Bucle for...of  para recorrer Listas o arrays

const array = [1, 2, 3, 4, 5];

for (let valor of array) {
     console.log(`for...of: ${valor}`);
}


//equivalente a recorrerlo indice por indice
for (let i=array.length; i >= 0; i--){
    console.log(array[i])
}
