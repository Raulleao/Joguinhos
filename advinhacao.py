from random import choice

listaNivel1 = list(range(0, 10+1))
listaNivel2 = list(range(0, 20+1))
listaNivel3 = list(range(0, 30+1))


def jogar_advinhacao():

    while True:

        def apresentacao():  # Apresenta o nome do jogo
            print("\033[31m=\033[m"*30)
            print("     \033[31mJogo da Adivinhação\033[m")
            print("\033[31m=\033[m"*30)

        def explicaJogo():  # explica o jogo
            print("O jogo é bem simples e dividido em duas partes:\n"
                  "1- Escolha o nível do jogo\n"
                  "2- Digite um número e torça para acertar"
                  )

        def nivelJogo():
            print("\033[31m=\033[m"*15)
            print("     \033[31mNível\033[m")
            print("\033[31m=\033[m"*15)
            print("\033[34m1- Fácil\n"
                  "2- Médio\n"
                  "3- Difícil\033[m\n")
            while True:
                global nivelJogador
                nivelJogador = int(input("Digite o nível que deseja jogar: "))
                if nivelJogador == 1 or nivelJogador == 2 or nivelJogador == 3:
                    print(f"Nivel escolhido: {nivelJogador}")
                    break

        def jogador():
            while True:
                global escolhaJogador
                print("\033[31mNível fácil digite um número entre 0 e 10\n"
                      "Nível médio digite um número entre 0 e 20\n"
                      "Nível difícil digite um número entre 0 e 30\n\033[m")

                escolhaJogador = int(input("Resposta: "))

                if nivelJogador == 1 and escolhaJogador >= 0 and escolhaJogador <= 10:
                    break
                if nivelJogador == 2 and escolhaJogador >= 0 and escolhaJogador <= 20:
                    break
                if nivelJogador == 3 and escolhaJogador >= 0 and escolhaJogador <= 30:
                    break

        def computador():
            global escolhaComputador
            if nivelJogador == 1:
                escolhaComputador = choice(listaNivel1)
            elif nivelJogador == 2:
                escolhaComputador = choice(listaNivel2)
            elif nivelJogador == 3:
                escolhaComputador = choice(listaNivel3)

        def vencedor():
            if nivelJogador == 1:
                escolhaComputador = choice(listaNivel1)
                if escolhaJogador == escolhaComputador:
                    print("JOGADOR VENCEU")
                else:
                    print("COMPUTADOR VENCEU")

            elif nivelJogador == 2:
                escolhaComputador = choice(listaNivel2)
                if escolhaJogador == escolhaComputador:
                    print("JOGADOR VENCEU")
                else:
                    print("COMPUTADOR VENCEU")

            elif nivelJogador == 3:
                escolhaComputador = choice(listaNivel3)
                if escolhaJogador == escolhaComputador:
                    print("JOGADOR VENCEU")
                else:
                    print("COMPUTADOR VENCEU")
            print(f"\033[31mO jogador escolheu: {escolhaJogador}\n"
                  f"O computador escolheu: {escolhaComputador}\033[m")

        apresentacao()
        print()

        explicaJogo()
        print()

        nivelJogo()
        print()

        jogador()
        print()

        computador()
        print()

        vencedor()
        print()

        contounao = str(input('Deseja continuar [S/N]?')).upper().strip()[0]
        if contounao == 'N':
            print('\033[31mFIM DO PROGRAMA\033[m')
            break


if __name__ == "__main__":
    jogar_advinhacao()
