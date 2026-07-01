// EXERCÍCIO 4 - Sistema de Controle Financeiro
 
function calcularTotalGastos(gastos) {
  var total = 0;
 
  for (var i = 0; i < gastos.length; i++) {
    var valorNumero = Number(gastos[i]);
 
    if (isNaN(valorNumero)) {
      continue; 
    }
 
    total = total + valorNumero;
  }
 
  return total;
}
 
function exibirGastos(gastos) {
  var total = calcularTotalGastos(gastos);
 
  console.log("Total: R$ " + total);
  console.log("");
 
  if (total > 2000) {
    console.log("Limite ultrapassado");
  } else {
    console.log("Gastos dentro do limite");
  }
  console.log("----------------------------------");
}
 
var gastos1 = ["500", "350.50", "1000"];
var gastos2 = ["800", "900", "700"];
 
exibirGastos(gastos1);
exibirGastos(gastos2);