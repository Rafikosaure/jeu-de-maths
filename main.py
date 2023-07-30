import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 0


def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 2)
    # 0 -> +
    # 1 -> *
    # 2 -> -
    operateur_str = "+"
    if o == 1:
        operateur_str = "x"
    elif o == 2:
        operateur_str = "-"
    while True:
        reponse_str = input(f"Calcule : {a} {operateur_str} {b} = ")
        try:
            reponse_int = int(reponse_str)
            calcul = a+b
            if o == 1:
                calcul = a*b
            elif o == 2:
                calcul = a-b
            if reponse_int == calcul:
                return True
            break
        except:
            print("Réponse invalide !")
    return False


print()
print("Bienvenue dans le jeu de maths !")
print()

while True:
    while True:
        NB_QUESTIONS_STR = input("Sur combien de questions souhaites-tu t'exercer ? ")
        if NB_QUESTIONS_STR != "0":
            try:
                NB_QUESTIONS = int(NB_QUESTIONS_STR)
                print("C'est parti !")
                print()
                break
            except:
                print("Réponse invalide !")
        else:
            print("A bientôt !")
            input()
            quit()

    nb_points = 0
    for i in range(0, NB_QUESTIONS):
        print(f"Question n°{i+1} sur {NB_QUESTIONS}:")
        if poser_question():
            print("Bonne réponse !")
            nb_points += 1
        else:
            print("Mauvaise réponse !")
        if nb_points == 1:
            print(f"Tu as {nb_points} point.")
            print()
        else:
            print(f"Tu as {nb_points} points.")
            print()

    print(f"Ta note est de {nb_points}/{NB_QUESTIONS}.")

    moyenne = int(NB_QUESTIONS/2)
    if nb_points == NB_QUESTIONS:
        print("Excellent !")
    elif nb_points == 0:
        print("Tu devrais réviser tes maths !")
    elif nb_points > moyenne:
        print("Pas mal !")
    else:
        print("Tu peux faire mieux.")

    print()
    recommencer_serie = input('Souhaites-tu recommencer une série de questions ? (tape "o" pour oui): ')
    if recommencer_serie != "o":
        print("A bientôt !")
        break

input()

