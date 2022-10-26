alphabet='abcdefghijklmnopqrstuvwxyz'
alphabet_latin='abcdefghijklmnopqrstuvwxyzéèêëēėęàáâäæãåāôöòóœøōõûüùúūîïíīįìÿçćč'
def error(n):
    errors=["exception non gérée.",
    "vous devez choisir un nombre entre un et deux. Veuillez réessayer.",
    "Erreur, votre texte ne doit contenir que des lettres.",
    "Aucun fichier 'cesar.txt' dans le dossier.",
    "Ce n'est pas une lettre."
    ]
    print(colored("/!\ Erreur, "+errors[n],255,0,0))
def colored(text,r=200,g=200,b=200):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r,g,b,text)
