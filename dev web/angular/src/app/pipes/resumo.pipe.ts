import { Pipe, PipeTransform } from '@angular/core';

/**
 * Pipe customizado (conceito de Pipes do Angular).
 * Resume um texto para um número máximo de caracteres, adicionando "..."
 * quando o texto é cortado.
 *
 * Uso no template: {{ produto.descricao | resumo:60 }}
 */
@Pipe({
  name: 'resumo',
  standalone: true,
})
export class ResumoPipe implements PipeTransform {
  transform(valor: string, tamanho = 80): string {
    if (!valor) {
      return '';
    }
    if (valor.length <= tamanho) {
      return valor;
    }
    return `${valor.slice(0, tamanho).trim()}...`;
  }
}
