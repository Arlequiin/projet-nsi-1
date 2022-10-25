def error(n):
    errors={
    0:"Problème technique...\nCela ne peut être du qu'à une erreur de programmation.",
    1:"/!\ Erreur, vous devez choisir un nombre entre un et deux. Veuillez réessayer.",
    2:"/!\ Erreur, votre texte ne doit contenir que des lettres."
    }
    print(colored("Erreur, vous devez choisir un nombre entre un et deux. Veuillez réessayer.",255,0,0))
def colored(text,r=255,g=255,b=255):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r,g,b,text)
