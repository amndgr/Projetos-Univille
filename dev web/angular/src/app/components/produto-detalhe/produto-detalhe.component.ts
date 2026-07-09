import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, ActivatedRoute } from '@angular/router';
import { Produto } from '../../models/produto.model';
import { ProdutoService } from '../../services/produto.service';
import { ResumoPipe } from '../../pipes/resumo.pipe';

@Component({
  selector: 'app-produto-detalhe',
  standalone: true,
  imports: [CommonModule, RouterLink, ResumoPipe],
  templateUrl: './produto-detalhe.component.html',
})
export class ProdutoDetalheComponent {
  private readonly rotaAtiva = inject(ActivatedRoute);
  private readonly produtoService = inject(ProdutoService);

  // O parâmetro ":id" da URL é lido a partir do ActivatedRoute (Routing)
  readonly produto: Produto | undefined = this.produtoService.buscarPorId(
    this.rotaAtiva.snapshot.params['id']
  );

  linkWhatsapp(nomeProduto: string): string {
    const mensagem = encodeURIComponent(
      `Olá! Quero encomendar o(a) ${nomeProduto} 🧶`
    );
    return `https://wa.me/5547996838981?text=${mensagem}`;
  }
}
