// Sistema de Matrícula Acadêmica

function exibirDisciplinas(disciplinas) {
  for (var i = 0; i < disciplinas.length; i++) {
    console.log(disciplinas[i]);
  }

  console.log("");
  console.log("Total: " + disciplinas.length);
  console.log("");

  if (disciplinas.includes("JavaScript")) {
    console.log("Aluno cursa JavaScript");
  } else {
    console.log("Aluno não cursa JavaScript");
  }

  // adicionar uma nova disciplina
  disciplinas.push("Inglês");
  console.log("Nova disciplina adicionada: " + disciplinas[disciplinas.length - 1]);
  console.log("----------------------------------");
}

function percorrerDisciplinas(disciplinas) {
  for (var i = 0; i < disciplinas.length; i++) {
    var disciplinaAtual = disciplinas[i];

    if (disciplinaAtual === "") {
      continue; // ignora disciplinas vazias
    }

    console.log(disciplinaAtual);

    if (disciplinaAtual === "TCC") {
      console.log("");
      console.log("Laço interrompido");
      break; // encerra o laço ao encontrar TCC
    }
  }
  console.log("----------------------------------");
}

var disciplinas1 = ["HTML", "CSS", "JavaScript"];
var disciplinas2 = ["Banco de Dados", "", "TCC", "Redes"];

exibirDisciplinas(disciplinas1);
percorrerDisciplinas(disciplinas2);
