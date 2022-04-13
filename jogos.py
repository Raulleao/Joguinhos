import forca
import advinhacao


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Digite aqui o jogo que quer jogar: "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        advinhacao.jogar_advinhacao()


if __name__ == "__main__":
    escolhe_jogo()
