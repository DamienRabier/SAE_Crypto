import string



texte_chiffre = "Zc krgfkr u'le ufzxk le rzi drikzrc jli c'fscfex tyrjjzj ul mrjzjkrj.Zc flmizk jfe wizxf dlirc, zc gizk ul crzk wifzu, zc slk le xireu sfc. Zc j'rgrzjrzk. Zc j'rjjzk jli jfe tfjp, zc gizk le aflierc hl'zc gritflilk u'le rzi uzjkirzk. Zc rccldr le tzxrizccf hl'zc wldr aljhl'rl sflk hlfzhl'zc kiflmrk jfe griwld ziizkrek. Zc kfljjr."
alphaMap = {"A":8.4,"B":1.05,"C":3.03,"D":4.18,"E":17.26,"F":1.12,"G":1.27,"H":0.92,"I":7.34,"J":0.31,"K":0.05,"L":6.01,"M":2.96,"N":7.13,"O":5.26,"P":3.01,"Q":0.99,"R":6.55,"S":5.08,"T":7.07,"U":5.74,"V":1.32,"W":0.04,"X":0.45,"Y":0.30,"Z":0.12}
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def dic_freq(texte):
    """Renvoie un dictionnaire contenant la fréquence d'apparition de chaque lettre de l'alphabet dans le texte

    Args:
        texte (String): Le texte à analyser

    Returns:
        dict: Un dictionnaire contenant la fréquence d'apparition de chaque lettre de l'alphabet dans le texte
    """
    dic = {}
    texte = texte.upper()
    for lettre in alpha:
        dic[lettre] = 0 # Initialisation du dictionnaire
    
    for lettre in texte:
        if lettre in alpha:
            dic[lettre] += 1 # Incrémentation de la fréquence de la lettre
    for lettre in dic:
        dic[lettre] = dic[lettre]/len(texte)*100 # Calcul de la fréquence de la lettre
    return dic
    
def distanceFreq(texte:string):
    """Calcule la distance entre la fréquence d'apparition des lettres dans le texte et la fréquence d'apparition des lettres dans la langue française

    Args:
        texte (string): Le texte à analyser

    Returns:
        float: La distance entre la fréquence d'apparition des lettres dans le texte et la fréquence d'apparition des lettres dans la langue française
    """
    freq = dic_freq(texte)
    distance = 0
    for lettre in alpha:
        distance += abs(freq[lettre] - alphaMap[lettre])# Calcul de la distance entre la fréquence d'apparition de la lettre dans le texte et la fréquence d'apparition de la lettre dans la langue française
    return distance


def dechiffrement_cle_decalage(texte_chiffre, cle_decalage):
    """Déchiffre un texte chiffré par décalage de cle_decalage

    Args:
        texte_chiffre (string): Le texte à déchiffrer
        cle_decalage (int): La clé de décalage

    Returns:
        string: Le texte déchiffré
    """
    texte_clair = ""
    for lettre in texte_chiffre:
        if lettre in string.ascii_letters: # Si la lettre est une lettre de l'alphabet
            if lettre.isupper():
                texte_clair += chr((ord(lettre) - cle_decalage - 65) % 26 + 65) # Décalage de la lettre
            else:
                texte_clair += chr((ord(lettre) - cle_decalage - 97) % 26 + 97) # Décalage de la lettre
        else:
            texte_clair += lettre # Si la lettre n'est pas une lettre de l'alphabet, on ne la décale pas
    return texte_clair

def essaie_decriptage_cle(texte_chiffre):
    """Force le déchiffrement d'un texte chiffré par décalage

    Args:
        texte_chiffre (string): Le texte à déchiffrer

    Returns:
        string: Le texte déchiffré
    """
    res = ""
    distance_min = distanceFreq(texte_chiffre)
    decal_min = 0
    for indice_decal in range(1,26):
        res = dechiffrement_cle_decalage(texte_chiffre,indice_decal) # Déchiffrement du texte
        distance = distanceFreq(res) # Calcul de la distance entre la fréquence d'apparition des lettres dans le texte et la fréquence d'apparition des lettres dans la langue française
        if distance < distance_min: # Si la distance est plus petite que la distance minimale
            distance_min = distance # On met à jour la distance minimale
            decal_min = indice_decal # On met à jour le décalage minimal 
    return dechiffrement_cle_decalage(texte_chiffre,decal_min%26) # On renvoie le texte déchiffré avec le décalage minimal



def main():
    continuer = True
    while continuer:
        texte = input("\n\n\n         Entrez le texte à déchiffrer:      \n\n\n")
        print("\n\n\n")
    
        print(essaie_decriptage_cle("\n\n"+texte+"\n\n"))
        print("\n\n\n")
        
        continuer = input("Voulez-vous continuer? (O/N) ").upper() != "N"
    
if __name__ == "__main__":
    main()
        
        
