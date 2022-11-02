from turtle import *
from functions import *
#Projet chiffrement de cesar
def to_list_of_indexes(charset):
   charset=charset.lower()
   list_of_indexes=[]
   for char in charset:
      if char in alphabet:
       list_of_indexes.append(alphabet.index(char))
      else:
         list_of_indexes.append(char)
   return list_of_indexes
def encode(charset,cesar_degree=3):
   indexes=to_list_of_indexes(charset)
   output=[]
   for index in indexes:
    if type(index)==int:
      diff=index+cesar_degree
      if diff>len(alphabet)-1:
         diff=0+(diff-(len(alphabet)))
      output.append(alphabet[diff])
    else:
      output.append(index)
   output=''.join(output).capitalize()
   return output
def decode(charset,cesar_degree=-3):
   return encode(charset,cesar_degree)
print("βοnjοur, quε sοuηαιτεz-vous fαιre?")
while True:
 try:
    operation_choice={'1':'encode','2':'decode'}[input("1. ΕΝCΟΔΕ/ 2. ΔΕCΟΔΕ\n>>> ")]
    break
 except:
    error(1)
print(f"Comment voulez-vous {operation_choice}r ?")
while True:
 try:
  type_choice={'1':'input','2':'file'}[input(f"1. Σαιsιr du τεχτε / 2. ficηιεr\n>>> ")]
  break
 except:
   error(1)

if type_choice=='input':
 print(colored(f"Saisissez le texte à {operation_choice} 🔒",0,0,200))
 try:
   a=(eval(f"{operation_choice}(input('>>> '))"))
   print(a)
   color('blue')
   write(a,font=("Arial", 16, "normal"))
   mainloop()
 except:
   error(0)
elif type_choice=='file':
   input(colored("Nommez votre fichier 'file.txt' et mettez-le dans le dossier 'projet-nsi-1', appuyez ensuite sur Entrée.",0,0,200))
   try:
      with open('file.txt','r') as f:
         content=f.read()
      with open('file.txt','w') as f2:
         f2.write(eval(operation_choice+"(content)"))
         print(colored("Votre fichier a été modifié avec succès!",0,100,150))
      write(eval(operation_choice+"(content)"),font=("Arial", 16, "normal"))
      mainloop()
   except:
      error(0)
print(colored("Fin de l'exécution",0,255,0))