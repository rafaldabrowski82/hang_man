import random
import sys

HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""
                ]


CATEGORY = {
    "Zwierzęta": ['MRÓWKA', 'PAWIAN', 'BÓBR', 'NIETOPERZ', 'NIEDŹWIEDŹ'],
    "Filmy": ['SPIDERMAN', 'BATMAN', 'IRONMAN', 'VENOM', 'RONIN']
}

# We choose random key from our dictionary
categoryPass = random.choice(list(CATEGORY.keys()))

# We choose random value from the key above
password = random.choice(CATEGORY[categoryPass])


def main():
    print("Wisielec, autor: Rafał Dąbrowski, rafaldabrowski82@gmail.com", end="\n\n")

    lista = list(password)
    lista1 = "_" * len(lista)
    lista1 = list(lista1)

    i = 0

    while True:
        print("Kategoria ukrytego słowa to: ", categoryPass, password)
        print(HANGMAN_PICS[i], end="\n\n")
        print(" ".join(lista1), end="\n\n")
        choosen = input("Podaj swoją literę: ")
        if not choosen.isalpha():
            continue
        choosen = choosen.upper()

        if HANGMAN_PICS[i] == HANGMAN_PICS[6]:
            print(HANGMAN_PICS[7])
            return print("Przegrałeś!!!")
        elif not choosen in lista:
            print("Brak tej literki w haśle")
            i += 1
        elif choosen in lista:
            # print(lista.count(choosen))
            nextIndex = 0
            for j in range(lista.count(choosen)):
                index = lista.index(choosen, nextIndex)
                lista1[index] = choosen
                nextIndex = index + 1

                if lista == lista1:
                    return print('Gratuluje, wygrałeś!!!')


main()
