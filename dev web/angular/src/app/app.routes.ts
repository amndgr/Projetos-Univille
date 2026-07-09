import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { ProdutoDetalheComponent } from './components/produto-detalhe/produto-detalhe.component';

/**
 * Rotas da aplicação (conceito de Routing do Angular).
 * A rota 'produto/:id' usa um parâmetro de rota para reaproveitar o mesmo
 * componente na exibição de qualquer um dos produtos do catálogo.
 */
export const routes: Routes = [
  { path: '', component: HomeComponent, title: 'Fio Encantado — Amigurumis Artesanais' },
  { path: 'produto/:id', component: ProdutoDetalheComponent, title: 'Fio Encantado — Produto' },
  { path: '**', redirectTo: '' },
];
