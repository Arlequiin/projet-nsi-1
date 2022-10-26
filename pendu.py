from turtle import *
from random import choice
from functions import *
while True:
    try:
        word_choice={'1':'random','2':'definied'}[input(colored("1. Mot aléatoire / 2. Choisir un mot\n>>> ",150,150,150))]
        break
    except:
        error(1)
if word_choice=='random':
 while True:
    try:
     lettres_max={'1':5,'2':10,'3':15}[input(colored("1. Facile / 2. Normal / 3. Difficile\n>>> ",150,150,150))]
     break
    except:
     error(4)
 print(colored(f"Bonjour. Un mot sera choisi aléatoirement dans le dictionnaire. Ce mot fera {lettres_max} lettres.",0,100,100))
 with open("dico.txt") as f:
    dico=f.readlines()
 mots_valables=[]
 for word in dico:
    if len(word)==lettres_max+1:
        mots_valables.append(word)
 mot=choice(mots_valables).replace('\n','').upper()
else:
    mot=input(colored("Veuillez saisir votre mot\n>>> ",150,150,200)).upper()
    lettres_max=len(mot)
    print("SCROLL = TRICHER\n"*20)
input(colored("*"*10+f"\nCOMMENT JOUER?\nSaisir une lettre.\nVous avez droit à {lettres_max} échecs.\n"+"*"*10,200,0,200))
to_compare=['_' for i in range(lettres_max)]
attempts=lettres_max
unavailable=[]
decomps=[lettres_max-2*(int(lettres_max/2)),int(lettres_max/2)]
print(decomps)
speed(1000)
while attempts>0:
    clear()
    print('-'*10)
    print(to_compare)
    penup()
    color('black')
    goto(-Screen().window_width()/3,Screen().window_height()/3)
    pendown()
    write(' '.join(to_compare),font=("Arial", 30, "normal"))
    print(attempts)
    if attempts<=lettres_max-(decomps[0]):
            print("oui")
            penup()
            goto(0,0)
            pendown()
            color('blue')
            for i in range(4):
                left(90)
                forward(Screen().window_width()/10)
                
    if attempts<=lettres_max-decomps[1]:
        left(90)
        forward(3*Screen().window_height()/10)
        right(90)
    if attempts<decomps[1]:
        left(180)
        forward(2*Screen().window_width()/10)
        right(180)
    penup()
    goto(Screen().window_width()/3,0)
    pendown()
    color('gray')
    write(f"Essais : {attempts}",font=("Arial", 20, "bold"))
    print(unavailable)
    penup()
    color('red')
    goto(-Screen().window_width()/3,-Screen().window_height()/4)
    pendown()
    write(' '.join(unavailable),font=("Arial", 25, "normal"))
    print('-'*10)
    a=textinput("Saisir une lettre", "Pendu").upper()
    if a in mot:
        for i in range(len(mot)):
            if mot[i]==a:
                to_compare[i]=a
    else:
        if a not in unavailable:
         unavailable.append(a+'\u0336')
        attempts-=1
    if to_compare==list(mot):
        print(colored("win",0,255,0))
        color('green')
        penup()
        goto(0,0)
        pendown()
        write('GAGNÉ',font=("Serif", 50, "bold"))
        penup()
        goto(0,-Screen().window_height()/10)
        pendown()
        color('blue')
        write(f"Le mot était {mot}.",font=("Serif", 25, "bold"))
        break
    elif attempts==0:
        penup()
        color('blue')
        goto(-2*Screen().window_width()/10,3*Screen().window_height()/10)
        pendown()
        left(90)
        forward(-Screen().window_height()/10)
        circle(Screen().window_height()/75)
        forward(-Screen().window_height()/40)
        left(90)
        forward(Screen().window_width()/50)
        forward(-Screen().window_width()/25)
        forward(Screen().window_width()/50)
        right(90)
        forward(-Screen().window_height()/40)
        right(45)
        forward(-Screen().window_height()/60)
        forward(Screen().window_height()/60)
        left(90)
        forward(-Screen().window_height()/60)
        print(colored('lose',255,0,0))
        color('red')
        penup()
        goto(0,0)
        pendown()
        write('PERDU',font=("Serif", 50, "bold"))
        penup()
        goto(0,-Screen().window_height()/10)
        pendown()
        color('blue')
        write(f"Le mot était {mot}.",font=("Serif", 25, "bold"))
print(colored(f"Le mot était {mot}.",0,100,100))
mainloop()