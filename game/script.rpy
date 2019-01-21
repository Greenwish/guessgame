init:
    image landscape = Image("fond.jpg")
    image elle = Image("char.png")
    image happy = Image("happy.png")
    image angry = Image("angry.png")
    image landscape2 = Image("fond2.jpg")
    image elle2 = Image("char2.png")
    image happy2 = Image("happy2.png")
    image angry2 = Image("angry2.png")
    image landscape3 = Image("fond3.jpg")
    image elle3 = Image("char3.png")
    image happy3 = Image("happy3.png")
    image angry3 = Image("angry3.png")
    image landscape4 = Image("fond4.jpg")

label start:
    $ e = Character("Elle")
    $ h = Character("Mini-elle")
    scene landscape
    show elle
    $ a = renpy.random.randint(1, 999)
    $ c = int(0)
    $ d = 0

    e "J'ai choisi un nombre inclu entre 1 et 999, devine le !"
    e "Je vais compter tes essais"
    while True:
        python:
            w = renpy.input("Quel est ton choix ?")
            w = w.strip()
            b = int(w)
        if a > b:
            show angry
            e "Ce n'est pas le bon nombre, le tien est trop petit"
            python:
                global c
                c += 1
        elif a < b:
            show angry
            e "Ce n'est pas le bon nombre, le tien est trop grand"
            python:
                global c
                c += 1
        elif a == b:
            show happy
            python:
                global c
                c += 1
            e "Bravo !!! Tu as réussi en [c] essais."
            e "J'ai faim... On va en ville ?"
            e "Je dois juste me changer avant, tu viens ?"
            scene landscape3
            show elle
            e "Tu m'attends 2 minutes ?"
            hide elle
            show elle3
            h "Bonjour, tu veux jouer en attendant ?"
            h " On va faire le jeu du pierre papier ciseaux"
            h "Voici les règles:"
            h "La pierre bat les ciseaux"
            h "Les ciseaux battent la pierre"
            h "Le papier bat la pierre"
            jump second

label second:
    $ e = Character("Elle")
    $ h = Character("Mini-elle")
    scene landscape3
    show happy3
    python:
        while True:
            user_choice = renpy.input('1 pour pierre\n2 pour papier\n3 pour ciseaux')
            user_choice = user_choice.strip()
            computer_choice = renpy.random.choice(['1', '2', '3'])
            if computer_choice == user_choice:
                h("Ex aequo")
            elif computer_choice == "1" and user_choice == "2":
                h("J'ai choisi la pierre!")
                h("Gagné!")
            elif computer_choice == "1" and user_choice == "3":
                h("J'ai choisi la pierre!")
                h("Perdu!")
            elif computer_choice == "2" and user_choice == "1":
                h("J'ai choisi papier!")
                h("Perdu!")
            elif computer_choice == "2" and user_choice == "3":
                h("J'ai choisi papier!")
                h("Gagné!")
            elif computer_choice == "3" and user_choice == "1":
                h("J'ai choisi ciseaux!")
                h('Gagné!')
            elif computer_choice == "3" and user_choice == "2":
                h("J'ai choisi ciseaux!")
                h("Perdu!")
            else:
                h("J'ai dit 1, 2 ou 3 !!!")
            play_again = renpy.input("Rejouer ? oui/non")
            if play_again == "non":
                break
    hide happy3
    show angry3
    h "Déjà ? Je m'amusais moi..."
    hide angry3
    show happy2
    e "Merci de m'avoir attendu, on y va ?"
    jump third

label third:
    $ e = Character("Elle")
    scene landscape2
    show elle2
    e "J'espère que ma soeur ne t'as pas trop embêté..."
    e "Allez, à ton tour de choisir un chiffre, je vais essayer de le deviner"
    e "On va rester sur un chiffre de 1 a 999"
    e "Prêt ?"
    hide elle2
    show angry2
    python:
        i = 0
        j = 1000
        m = 500
        counter = 1
        e("Tu as choisi [m] ?")
        condition = renpy.input("0 pour trop petit\n1 si j'ai trouvé\n2 pour trop grand")
        condition = condition.strip()
        condition = int(condition)
        while condition != 1:
            counter += 1
            if condition == 0:
                i = m + 1
            elif condition == 2:
                j = m - 1
            m = (i + j) / 2
            e("Tu as choisi [m] ?")
            condition = renpy.input("0 pour trop petit\n1 si j'ai trouvé\n2 pour trop grand")
            condition = condition.strip()
            condition = int(condition)
    hide angry2
    show happy2
    e "J'ai reussi ! Il m'a fallu [counter] essais."
    hide happy2
    scene landscape4
    "Le jeu est terminé souhaitez-vous le recommencer?"
    $ play_again = renpy.input("Rejouer ? oui/non")
    if play_again == "oui":
        jump start
    else:
        $ renpy.quit()
