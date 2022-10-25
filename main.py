from turtle import *
from functions import *
#Projet chiffrement de cesar
alphabet='abcdefghijklmnopqrstuvwxyz'
def to_list_of_indexes(charset):
   charset=charset.lower()
   list_of_indexes=[]
   for char in charset:
      list_of_indexes.append(alphabet.index(char))
   return list_of_indexes
def encode(charset,cesar_degree=3):
   indexes=to_list_of_indexes(charset)
   output=[]
   for index in indexes:
      output.append(alphabet[index+cesar_degree])
   output=''.join(output).capitalize()
   return output
a=input("βοnjοur, quε sοuηαιτεz-vous fαιre?\n 1. ΔΕCΟΔΕ / 2. ΕΝCΟΔΕ\n>>> ")
while True:
 try:
    operation_choice={'1':'encode','2':'decode'}[a]
    break
 except:
    error(1)
    a=input("1. ΔΕCΟΔΕ / 2. ΕΝCΟΔΕ\n>>> ")
print(f"Comment voulez-vous {operation_choice}r ?")
while True:
 try:
  type_choice={'1':'input','2':'choice'}[input(f"1. Σαιsιr du τεχτε / 2. ficηιεr\n>>> ")]
  break
 except:
   error(1)
if type_choice=='input':
 base_text=input(colored(f"Saisissez le texte à {operation_choice} 🔒\n>>> ",0,0,200))
 if operation_choice=='encode':
   while True:
    try:
     print(encode(input(">>> ")))
     break
    except:
      error(2)
print(colored("Fin de l'exécution",0,0,255))
