// Sistema de Cadastro de Produtos

function exibirProduto(produto) {
  console.log("Produto: " + produto.nome);
  console.log("Categoria: " + produto.categoria);

  var precoNumero = Number(produto.preco); 

  if (isNaN(precoNumero)) {
    console.log("Preço inválido");
    return;
  }

  console.log("Preço: R$ " + produto.preco);
  console.log("");

  if (produto.estoque < 10) {
    console.log("Estoque baixo");
  } else {
    console.log("Estoque adequado");
  }

  console.log("");

  for (var chave in produto) {
    console.log(chave + " = " + produto[chave] + " (tipo: " + typeof produto[chave] + ")");
  }

  console.log(Object.keys(produto));
  console.log("----------------------------------");
}

var produto1 = {
  nome: "Monitor",
  categoria: "Informática",
  preco: "899.90",
  estoque: 5
};

var produto2 = {
  nome: "Cadeira",
  categoria: "Escritório",
  preco: "450",
  estoque: 30
};

exibirProduto(produto1);
exibirProduto(produto2);
