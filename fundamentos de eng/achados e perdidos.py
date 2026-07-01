"""
Sistema de Achados e Perdidos - Terminal

Projeto de fens: MVP simples para gerenciamento de itens
achados e perdidos, permitindo cadastrar, listar, buscar e
atualizar o status dos itens, sem precisar ir fisicamente
até o local para conferir se o item já chegou.

Os dados são salvos em um arquivo JSON (dados.json), então
as informações continuam disponíveis mesmo depois de fechar
o programa.
"""

import json
import os
from datetime import datetime

ARQUIVO_DADOS = "dados.json"


def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_dados(itens):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(itens, arquivo, ensure_ascii=False, indent=4)


def cadastrar_item(itens):
    print("\n--- Cadastro de item achado ---")
    nome = input("Nome do item (ex: Carteira, Mochila): ").strip()
    descricao = input("Descrição (cor, marca, detalhes): ").strip()
    categoria = input("Categoria (ex: Documentos, Eletrônicos, Roupas): ").strip()
    local = input("Local onde foi encontrado: ").strip()

    novo_item = {
        "id": gerar_novo_id(itens),
        "nome": nome,
        "descricao": descricao,
        "categoria": categoria,
        "local": local,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "status": "disponível"
    }

    itens.append(novo_item)
    salvar_dados(itens)
    print(f"\nItem cadastrado com sucesso! (ID: {novo_item['id']})")


def gerar_novo_id(itens):
    if not itens:
        return 1
    return max(item["id"] for item in itens) + 1


def listar_itens(itens, apenas_disponiveis=True):
    print("\n--- Itens cadastrados ---")

    if apenas_disponiveis:
        itens_para_mostrar = [item for item in itens if item["status"] == "disponível"]
    else:
        itens_para_mostrar = itens

    if not itens_para_mostrar:
        print("Nenhum item encontrado.")
        return

    for item in itens_para_mostrar:
        mostrar_item(item)


def mostrar_item(item):
    print(f"\nID: {item['id']}")
    print(f"Nome: {item['nome']}")
    print(f"Descrição: {item['descricao']}")
    print(f"Categoria: {item['categoria']}")
    print(f"Local: {item['local']}")
    print(f"Data de cadastro: {item['data']}")
    print(f"Status: {item['status']}")
    print("-" * 30)


def buscar_item(itens):
    print("\n--- Buscar item ---")
    termo = input("Digite o nome, descrição ou categoria do item: ").strip().lower()

    resultados = [
        item for item in itens
        if termo in item["nome"].lower()
        or termo in item["descricao"].lower()
        or termo in item["categoria"].lower()
    ]

    if not resultados:
        print("\nNenhum item encontrado com esse termo.")
        return

    print(f"\n{len(resultados)} item(ns) encontrado(s):")
    for item in resultados:
        mostrar_item(item)


def atualizar_status(itens):
    print("\n--- Atualizar status de item ---")
    try:
        id_item = int(input("Digite o ID do item: "))
    except ValueError:
        print("ID inválido.")
        return

    item = next((i for i in itens if i["id"] == id_item), None)

    if not item:
        print("Item não encontrado.")
        return

    mostrar_item(item)
    print("Novo status:")
    print("1 - Disponível")
    print("2 - Reivindicado")
    print("3 - Retirado")
    opcao = input("Escolha uma opção: ").strip()

    status_map = {"1": "disponível", "2": "reivindicado", "3": "retirado"}

    if opcao in status_map:
        item["status"] = status_map[opcao]
        salvar_dados(itens)
        print("Status atualizado com sucesso!")
    else:
        print("Opção inválida.")


def exibir_menu():
    print("\n===== SISTEMA DE ACHADOS E PERDIDOS =====")
    print("1 - Cadastrar item achado")
    print("2 - Listar itens disponíveis")
    print("3 - Listar todos os itens (incluindo retirados)")
    print("4 - Buscar item")
    print("5 - Atualizar status de um item")
    print("0 - Sair")


def main():
    itens = carregar_dados()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_item(itens)
        elif opcao == "2":
            listar_itens(itens, apenas_disponiveis=True)
        elif opcao == "3":
            listar_itens(itens, apenas_disponiveis=False)
        elif opcao == "4":
            buscar_item(itens)
        elif opcao == "5":
            atualizar_status(itens)
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida, tente novamente.")


if __name__ == "__main__":
    main()