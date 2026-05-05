import random

#menu
print("""
==================================
      🎯 JOGO DE ADIVINHAÇÃO
==================================
1 - Jogar
2 - Regras
3 - Sair
==================================
""")

choice = int(input("Selecione a opção desejada: "))

if choice == 1:
    num_jogadores = int(input("Escolha a quantidade de jogadores(1 a 3): "))
    if num_jogadores == 1:

        name = str(input("Selecione o nome do jogador: "))
        guess = int(input("Escolha um número de 1 a 10: "))

        num = random.randint(1, 10)

        if guess >= 1 and guess <= 10:

            if guess == num:
                print(f"Parabéns {name}, você acertou!🎉")
            else:
                print("Infelizmente você errou o chute :(")

            print(f"Chute: {guess} | Número sorteado: {num}")
        else: 
            print("Você precisa escolher um número de 1 a 10!")


    elif num_jogadores == 2:

        name = str(input("Selecione o nome do jogador: "))
        name2 = str(input("Selecione o nome do segundo jogador: "))

        guess = int(input(f"{name}, escolha um número de 1 a 10: "))
        guess2 = int(input(f"{name2}, escolha um número de 1 a 10: "))

        num = random.randint(1, 10)

        if (guess >= 1 and guess <= 10) and (guess2 >= 1 and guess2 <= 10):

            if guess == num and guess2 == num:
                print("Ambos acertaram!🎉")

            elif guess == num:
                print(f"{name} acertou!🎉")

            elif guess2 == num:
                print(f"{name2} acertou!🎉")

            else:
                print("Infelizmente ambos erraram o chute :(")

            print(f"{name}: {guess} | {name2}: {guess2} | Número: {num}")
        else: 
            print("Você precisa escolher um número de 1 a 10!")

    elif num_jogadores == 3:

        name = str(input("Selecione o nome do jogador: "))
        name2 = str(input("Selecione o nome do segundo jogador: "))
        name3 = str(input("Selecione o nome do terceiro jogador: "))

        guess = int(input(f"{name}, escolha um número de 1 a 10: "))
        guess2 = int(input(f"{name2}, escolha um número de 1 a 10: "))
        guess3 = int(input(f"{name3}, escolha um número de 1 a 10: "))

        num = random.randint(1, 10)

        if (guess >= 1 and guess <= 10) and (guess2 >= 1 and guess2 <= 10) and (guess3 >= 1 and guess3 <= 10):

            if guess == num and guess2 == num and guess3 == num:
                print("Todos acertaram!🎉")

            elif guess == num and guess2 == num:
                print(f"{name} e {name2} acertaram!🎉")

            elif guess == num and guess3 == num:
                print(f"{name} e {name3} acertaram!🎉")

            elif guess2 == num and guess3 == num:
                print(f"{name2} e {name3} acertaram!🎉")

            elif guess == num:
                print(f"{name} acertou!🎉")

            elif guess2 == num:
                print(f"{name2} acertou!🎉")

            elif guess3 == num:
                print(f"{name3} acertou!🎉")

            else:
                print("Infelizmente ninguém acertou o chute :(")
            
            print(f"{name}: {guess} | {name2}: {guess2} | {name3}: {guess3} | Número: {num}")
        else:
            print("Você precisa escolher um número de 1 a 10!")

    else:
        print("No mínino 1 jogador e no máximo 3 jogadores!")



elif choice == 2:
    print("""
        📜 REGRAS DO JOGO 🎯

        1 - O jogador deve escolher um número de 1 a 10.
        2 - O sistema irá sortear um número aleatório no mesmo intervalo.
        3 - Se o número escolhido for igual ao número sorteado, você vence.
        4 - Caso contrário, você perde.
        5 - Tente a sorte quantas vezes quiser!

        Boa sorte! 🍀
    """)
    
elif choice == 3:
    print("""
        ╔══════════════════════════════╗
        ║        JOGO ENCERRADO        ║
        ╚══════════════════════════════╝

        Você decidiu sair...
        Até a próxima! 👋

        🎯 O jogo sempre estará te esperando...
    """)

else:
    print("Selecione uma opção válida!")