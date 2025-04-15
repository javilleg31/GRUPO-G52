

//dado un mes indicar su nombre y nro de días.

let mes = 16

switch (mes) {
  case 1: nombreMes = 'ENERO con 31 días'; break;
  case 2: nombreMes = 'FEBRERO con 28 días'; break;
  case 3: nombreMes = ' con  días'; break;
  case 4: nombreMes = ' con  días'; break;
  case 5: nombreMes = ' con  días'; break;
  case 6: nombreMes = ' con  días'; break;
  case 7: nombreMes = ' con  días'; break;
  case 8: nombreMes = ' con  días'; break;
  case 9: nombreMes = ' con  días'; break;
  case 10: nombreMes = ' con  días'; break;
  case 11: nombreMes = ' con  días'; break;
  case 12: nombreMes = 'DICIEMBRE con 31 días'; break;
  default: nombreMes = 'mes no existe';
}

console.log(`${mes} es ${nombreMes}`)