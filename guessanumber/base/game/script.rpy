init:
    image landscape = Image("fond.jpg")
    image elle = Image("char.png")
    image happy = Image("happy.png")
    image angry = Image("angry.png")

label start:
    $ e = Character("Elle")
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
            e "Est-ce que tu veux rejouer ?"
            python:
                f = renpy.input("Quel est ton choix ? <oui/non>")
                f = f.strip()
            if f == "non":
                $ renpy.quit()
            else:
                e "Super !"
                jump start
