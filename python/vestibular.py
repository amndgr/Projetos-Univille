def avaliar_candidato(nome, portugues, matematica, conhecimentos):
    media = (portugues + matematica + conhecimentos) / 3
    aprovado = media > 7.0 and portugues >= 5.0 and matematica >= 5.0 and conhecimentos >= 5.0
    return {
        'nome': nome,
        'portugues': portugues,
        'matematica': matematica,
        'conhecimentos': conhecimentos,
        'media': media,
        'aprovado': aprovado,
    }
