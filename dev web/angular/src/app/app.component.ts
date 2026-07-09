import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink],
  templateUrl: './app.component.html',
})
export class AppComponent {
  // Interpolação: exibida diretamente no template (app.component.html)
  readonly nomeLoja = 'Fio Encantado';
  readonly contato = '(47) 9 9683-8981';
  readonly whatsapp = 'https://wa.me/5547996838981';
  readonly instagram = 'https://instagram.com/';

  readonly anoAtual = new Date().getFullYear();
}
