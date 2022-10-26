from turtle import *
from random import choice
from functions import *
lettres_max=10
input(colored(f"Bonjour. Un mot sera choisi aléatoirement dans le dictionnaire. Ce mot fera {lettres_max} lettres.",0,100,100))
with open("dico.txt") as f:
    dico=f.readlines()
mots_valables=[]
for word in dico:
    if len(word)==lettres_max+1:
        mots_valables.append(word)
mot=choice(mots_valables).replace('\n','').lower()
input(colored("*"*10+f"\nCOMMENT JOUER?\nSaisir une lettre.\nVous avez droit à {lettres_max} échecs.\n"+"*"*10,200,0,200))
to_compare=['-' for i in range(lettres_max)]
attempts=10
unavailable=[]
while attempts>0:
    print('-'*10)
    print(to_compare)
    print(attempts)
    print(unavailable)
    print('-'*10)
    a=input(">>> ")
    if a in mot:
        for i in range(len(mot)):
            if mot[i]==a:
                to_compare[i]=a
    else:
        if a not in unavailable:
         unavailable.append(a)
        attempts-=1
    if to_compare==list(mot):
        print(colored("win",0,255,0))
        break
    elif attempts==0:
        print(colored('lose',255,0,0))
print(colored(f"Le mot était {mot}.",0,100,100))