import string



texte_chiffre = "Zc krgfkr u'le ufzxk le rzi drikzrc jli c'fscfex tyrjjzj ul mrjzjkrj.Zc flmizk jfe wizxf dlirc, zc gizk ul crzk wifzu, zc slk le xireu sfc. Zc j'rgrzjrzk. Zc j'rjjzk jli jfe tfjp, zc gizk le aflierc hl'zc gritflilk u'le rzi uzjkirzk. Zc rccldr le tzxrizccf hl'zc wldr aljhl'rl sflk hlfzhl'zc kiflmrk jfe griwld ziizkrek. Zc kfljjr."

def separer_mots(texte):
    # Separe les mots d'un texte dans une liste
    mot_actuelle = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = list()
    for lettre in texte:
        if lettre in alphabet:
            mot_actuelle += lettre
        elif mot_actuelle != "":
            res.append(mot_actuelle)
            mot_actuelle = ""
    return res

def compter_nb_mots_francais(liste_de_mots,dictionnaire):
    with open(dictionnaire, encoding="utf-8") as file:
        words = set(line.strip() for line in file)
    nb_mots = 0
    for mots in liste_de_mots:
        mot = str.lower(mots)
        if mot in words:
            nb_mots+= 1
    return nb_mots



def dechiffrement_cle_decalage(texte_chiffre, cle_decalage):
    texte_clair = ""
    for lettre in texte_chiffre:
        if lettre in string.ascii_letters:
            if lettre.isupper():
                texte_clair += chr((ord(lettre) - cle_decalage - 65) % 26 + 65)
            else:
                texte_clair += chr((ord(lettre) - cle_decalage - 97) % 26 + 97)
        else:
            texte_clair += lettre
    return texte_clair

def essaie_decriptage_cle(texte_chiffre):
    res = ""
    indice_decal = 1
    bon_mot = False
    for indice_decal in range(1,26):
        res = dechiffrement_cle_decalage(texte_chiffre,indice_decal)
        if (compter_nb_mots_francais(separer_mots(res),"Utilitaires/francais.txt") > (len(separer_mots(res))/3)):
            return res
    return "Erreur: Ce texte n'est pas crypté avec le chiffrement de César"            

def main():
    continuer = True
    while continuer:
        texte = input("\n\n\n         Entrez le texte à déchiffrer:      \n\n\n")
        print(essaie_decriptage_cle("\n\n"+texte+"\n\n"))
        continuer = input("Voulez-vous continuer? (O/N) ") != "N"
    
if __name__ == "__main__":
    main()
        
        