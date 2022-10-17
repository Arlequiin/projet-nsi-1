from turtle import *
#Projet chiffrement de cesar
alphabet='abcdefghijklmnopqrstuvwxyz'
a=input("βοnjοur, quε sοuηαιτεz-vous fαιre? 1. ΔΕCΟΔΕ / 2. ΕΝCΟΔΕ\n>>> ")
while True:
 try:
    choice={'1':'encode','2':'decode'}[a]
    break
 except:
    print("Erreur, vous devez choisir un nombre entre un et deux. Veuillez réessayer.")
    a=input("1. ΔΕCΟΔΕ / 2. ΕΝCΟΔΕ\n>>> ")
print(choice)