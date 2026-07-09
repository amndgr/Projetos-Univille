import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { Produto } from '../../models/produto.model';
import { ProdutoService } from '../../services/produto.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './home.component.html',
})
export class HomeComponent {
  // Injeção de dependência: o serviço é obtido através do injetor do Angular
  private readonly produtoService = inject(ProdutoService);

  readonly produtos: Produto[] = this.produtoService.listarTodos();

  // Propriedade ligada ao campo de busca via two-way binding ([(ngModel)])
  termoBusca = '';

  // Event binding: método chamado a partir de (input) no template
  limparBusca(): void {
    this.termoBusca = '';
  }

  get produtosFiltrados(): Produto[] {
    const termo = this.termoBusca.trim().toLowerCase();
    if (!termo) {
      return this.produtos;
    }
    return this.produtos.filter((produto) =>
      produto.nome.toLowerCase().includes(termo)
    );
  }
}
