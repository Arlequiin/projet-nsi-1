from functions import *
import unidecode
#Projet Palindrome
a=input("Bonjour, quelle sera la méthode de saisie\n1. Manuelle / 2. Fichier\n>>> ")
if a=='1':
 text=unidecode.unidecode(input("Veuillez saisir votre phrase/mot\n>>> ").replace("\n",'').lower())
else:
 input(colored("Veuillez placer votre texte dans un fichier nommé 'file.txt' que vous placerez dans ce dossier, cliquez ensuite sur Entrée.",0,0,255))
 with open('file.txt','r') as f:
    content=f.read()
 text=unidecode.unidecode(content.replace("\n",'').lower())
text_clean=[]
for char in text:
    if char in alphabet:
        text_clean.append(char)
if text_clean==text_clean[::-1]:
    print("Palindrome")