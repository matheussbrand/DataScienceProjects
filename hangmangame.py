import random
import time

print("\nBem-Vindo ao Jogo da Forca\n")
name = input("Coloque seu  nome: ")
print("Olá " + name + "! Boa sorte!")
time.sleep(2)
print("O jogo vai começar!\n Vamos jogar!")
time.sleep(3)
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["janeiro","bolo","imagem","filme","missa","criança","casaco","brinquedo","dança","machucado","planta","ave","cachorro"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
   
def play_loop():
    global play_game
    play_game = input("Vamos jogar de novo? s = sim, n = não \n")
    while play_game not in ["s", "n","S","N"]:
        play_game = input("Quer jogar mais? s = sim, n = não \n")
    if play_game == "s":
        main()
    elif play_game == "n":
        print("Foi  muito divertido! Espero te ver logo!")
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("A palavra é: " + display + " Dê seu palpite: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Errou, tente outra letra\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Tente outra letra.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Palpite errado. " + str(limit - count) + " chances restantes\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Palpite errado. " + str(limit - count) + " chances restantes\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Palpite errado. " + str(limit - count) + " chances restantes\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Palpite errado. " + str(limit - count) + " última chance\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Palpite errado. Você foi enforcado!!!\n")
            print("A palavra era:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Parabéns! Você acertou!")
        play_loop()

    elif count != limit:
        hangman()


main()

hangman()