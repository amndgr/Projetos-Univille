import { Injectable } from '@angular/core';
import { Produto } from '../models/produto.model';

/**
 * @Injectable com providedIn: 'root' registra este serviço no injetor raiz
 * da aplicação, permitindo que qualquer componente o receba via
 * injeção de dependência (Dependency Injection), apenas declarando-o
 * no construtor.
 */
@Injectable({
  providedIn: 'root',
})
export class ProdutoService {
  private readonly produtos: Produto[] = [
    {
      id: 'coruja',
      nome: 'Corujinha',
      preco: 89.9,
      imagem: 'assets/coruja.jpeg',
      imagemAlt: 'Amigurumi Corujinha em crochê marrom com branco, 22 cm',
      descricao:
        'Corujinha em crochê marrom e branco, feito à mão ponto a ponto com linha 100% algodão. Rosto bordado com expressão gentil e muito charme.',
      altura: '22 cm',
      material: 'Algodão 100%',
      seguranca: 'Todas as idades',
      prazo: '5 a 7 dias úteis',
    },
    {
      id: 'serpente',
      nome: 'Serpente',
      preco: 74.9,
      imagem: 'assets/serpente.jpeg',
      imagemAlt: 'Amigurumi Serpente em crochê verde',
      descricao:
        'Serpente em crochê verde, macia e bem-humorada, feita à mão ponto a ponto com linha 100% algodão. Ótima companhia para todas as idades.',
      altura: '35 cm',
      material: 'Algodão 100%',
      seguranca: 'Todas as idades',
      prazo: '5 a 7 dias úteis',
    },
    {
      id: 'girafa',
      nome: 'Girafinha',
      preco: 99.0,
      imagem: 'assets/girafa.jpeg',
      imagemAlt: 'Amigurumi Girafa em crochê amarelo e marrom',
      descricao:
        'Girafinha em crochê amarelo com manchas em marrom, pescoço bem proporcionado e acabamento caprichado ponto a ponto.',
      altura: '28 cm',
      material: 'Algodão 100%',
      seguranca: 'Todas as idades',
      prazo: '5 a 7 dias úteis',
    },
    {
      id: 'leao',
      nome: 'Leãozinho',
      preco: 49.9,
      imagem: 'assets/leaozinho.jpeg',
      imagemAlt: 'Amigurumi Leãozinho em crochê laranja com detalhes em marrom',
      descricao:
        'Leãozinho em crochê laranja com juba em marrom, rostinho fofo e acabamento macio, perfeito para presentear.',
      altura: '18 cm',
      material: 'Algodão 100%',
      seguranca: 'Todas as idades',
      prazo: '5 a 7 dias úteis',
    },
    {
      id: 'tigre',
      nome: 'Tigrinho',
      preco: 55.0,
      imagem: 'assets/tigrinho.jpeg',
      imagemAlt: 'Amigurumi Tigre em crochê laranja e detalhes em preto e branco',
      descricao:
        'Tigrinho em crochê laranja com listras em preto e barriga branca, feito à mão com muito capricho nos detalhes.',
      altura: '20 cm',
      material: 'Algodão 100%',
      seguranca: 'Todas as idades',
      prazo: '5 a 7 dias úteis',
    },
    {
      id: 'zebra',
      nome: 'Zebrinha',
      preco: 69.0,
      imagem: 'assets/zebrinha.jpeg',
      imagemAlt: 'Amigurumi Zebra em crochê branco e preto',
      descricao:
        'Zebrinha em crochê branco com listras em preto, crina em relevo e acabamento delicado ponto a ponto.',
      altura: '24 cm',
      material: 'Algodão 100%',
      seguranca: 'Todas as idades',
      prazo: '5 a 7 dias úteis',
    },
  ];

  listarTodos(): Produto[] {
    return this.produtos;
  }

  buscarPorId(id: string): Produto | undefined {
    return this.produtos.find((produto) => produto.id === id);
  }
}
