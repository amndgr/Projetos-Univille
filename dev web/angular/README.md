# 🧶 Fio Encantado — Loja de Amigurumis (Angular)

Este é o projeto **Fio Encantado**, migrado de HTML/CSS estático para **Angular** (standalone components), como parte da atividade de Desenvolvimento Web.

## ⚠️ Antes de rodar: adicione as imagens

Copie as fotos dos produtos do projeto original para a pasta `public/assets/`, com estes nomes:

```
public/assets/coruja.jpeg
public/assets/serpente.jpeg
public/assets/girafa.jpeg
public/assets/leaozinho.jpeg
public/assets/tigrinho.jpeg
public/assets/zebrinha.jpeg
public/assets/favicon-96x96.png
```

## ▶️ Como rodar o projeto

```bash
npm install
npm start
```

Depois abra **http://localhost:4200** no navegador.

## 📦 Como publicar no GitHub

```bash
git init
git add .
git commit -m "Projeto Angular - Fio Encantado"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
git push -u origin main
```

Lembre-se de deixar o repositório **público** antes de enviar o link.

## 🧩 Conceitos de Angular implementados

| Conceito | Onde está no código |
|---|---|
| **Componentes** | `AppComponent`, `HomeComponent`, `ProdutoDetalheComponent` |
| **Interpolação `{{ }}`** | Nome da loja no cabeçalho/rodapé, nome e preço do produto |
| **Property binding `[ ]`** | `[src]`, `[alt]`, `[href]`, `[routerLink]`, `[attr.aria-label]` |
| **Event binding `( )`** | `(click)="limparBusca()"` no botão de limpar a busca |
| **Two-way binding `[( )]`** | `[(ngModel)]="termoBusca"` no campo de busca da home |
| **Diretiva estrutural `*ngIf`** | Mensagem de "nenhum resultado" e produto não encontrado |
| **Diretiva estrutural `*ngFor`** | Listagem dos cards de produtos na home |
| **Pipes** | `currency` (preço em R$) e `resumo` (pipe customizado, criado em `pipes/resumo.pipe.ts`) |
| **Services + Injeção de Dependência** | `ProdutoService` (`services/produto.service.ts`), injetado com `inject()` |
| **Roteamento (Routing)** | `app.routes.ts`, rota `produto/:id` com parâmetro dinâmico, `routerLink`, `ActivatedRoute` |

## 📁 Estrutura

```
src/app/
├── app.component.ts/html      → layout raiz (cabeçalho, router-outlet, rodapé)
├── app.routes.ts               → definição das rotas
├── app.config.ts               → configuração da aplicação standalone
├── models/produto.model.ts     → interface Produto
├── services/produto.service.ts → dados dos produtos + injeção de dependência
├── pipes/resumo.pipe.ts        → pipe customizado
└── components/
    ├── home/                   → página inicial (listagem + busca)
    └── produto-detalhe/        → página de detalhe do produto
```
