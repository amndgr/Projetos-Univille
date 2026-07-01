// =====================================================
// EXERCÍCIO 5 - Sistema Completo de Eventos
// =====================================================
 
function exibirEvento(evento) {
  console.log("Evento: " + evento.nome);
  console.log("Local: " + evento.local);
  console.log("");
 
  var dataFormatada = evento.data.toLocaleDateString("pt-BR");
  console.log(dataFormatada);
  console.log("");
 
  console.log("Participantes: " + evento.participantes.length);
  console.log("");
 
  if (evento.participantes.length > 0) {
    console.log("Existem participantes cadastrados");
  } else {
    console.log("Nenhum participante cadastrado");
  }
 
  console.log("");
  console.log("Local cadastrado: " + evento.hasOwnProperty("local"));
  console.log("");
 
  // exibir propriedades, valores e tipos
  for (var chave in evento) {
    console.log(chave + " = " + evento[chave] + " (tipo: " + typeof evento[chave] + ")");
  }
  console.log("----------------------------------");
}
 
var evento1 = {
  nome: "Semana da Tecnologia",
  local: "Auditório",
  data: new Date("2026-08-20"),
  participantes: ["Ana", "Carlos", "Marcos"]
};
 
var evento2 = {
  nome: "Workshop",
  local: "Laboratório 5",
  data: new Date("2026-09-10"),
  participantes: []
};
 
exibirEvento(evento1);
exibirEvento(evento2);