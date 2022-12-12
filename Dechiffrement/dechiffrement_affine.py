ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphaMap = {"A":8.4,"B":1.05,"C":3.03,"D":4.18,"E":17.26,"F":1.12,"G":1.27,"H":0.92,"I":7.34,"J":0.31,"K":0.05,"L":6.01,"M":2.96,"N":7.13,"O":5.26,"P":3.01,"Q":0.99,"R":6.55,"S":5.08,"T":7.07,"U":5.74,"V":1.32,"W":0.04,"X":0.45,"Y":0.30,"Z":0.12}
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def enlever_caractere_non_dico(texte):
    """Enlève les caractères non présents dans l'alphabet

    Args:
        texte (str): texte à traiter

    Returns:
        str: texte sans caractères non présents dans l'alphabet
    """
    texte = texte.upper()
    for mot in texte:
        if mot not in ALPHABET: # Si le mot n'est pas dans l'alphabet
            texte = texte.replace(mot, "") # On le remplace par une chaine vide
    return texte

def dic_freq(texte):
    """Calcule la fréquence d'apparition des lettres dans le texte

    Args:
        texte (str): texte à traiter

    Returns:
        dict: dictionnaire contenant la fréquence d'apparition des lettres
    """
    dic = {}
    texte = enlever_caractere_non_dico(texte) # On enlève les caractères non présents dans l'alphabet
    for lettre in alpha:
        dic[lettre] = 0
    
    for lettre in texte:
        if lettre in alpha:
            dic[lettre] += 1 # On incrémente la fréquence de la lettre
    for lettre in dic:
        dic[lettre] = dic[lettre]/len(texte)*100 # On divise par la longueur du texte pour avoir la fréquence
    return dic
    
def distanceFreq(texte):
    """Calcule la distance entre la fréquence d'apparition des lettres dans le texte et la fréquence d'apparition des lettres dans l'alphabet

    Args:
        texte (str): texte à traiter

    Returns:
        float: distance entre la fréquence d'apparition des lettres dans le texte et la fréquence d'apparition des lettres dans l'alphabet
    """
    freq = dic_freq(texte)
    distance = 0
    for lettre in alpha:
        distance += abs(freq[lettre] - alphaMap[lettre]) # On calcule la distance entre la fréquence d'apparition des lettres dans le texte et la fréquence d'apparition des lettres dans l'alphabet
    return distance
    
def pgcd(a, b):
    """Calcule le PGCD de deux nombres

    Args:
        a (int): premier nombre
        b (int): deuxième nombre
        
    Returns:
        int: PGCD de a et b
    """
    if(b == 0):
        return a # Si b est égal à 0, on retourne a
    else:
        return pgcd(b, a % b) # Sinon on retourne le PGCD de b et le reste de la division de a par b

def modulaire_inverse(a, n):
    """Calcule l'inverse modulaire de a modulo n

    Args:
        a (int): nombre dont on veut calculer l'inverse modulaire
        n (int): modulo
        
    Returns:
        int: inverse modulaire de a modulo n
    """
    for i in range(1, n):
        if((a * i) % n == 1): 
            return i # Si a * i est divisible par n, on retourne i
    return 1

def affine_decode(text, a, b):
    """ Déchiffre un texte chiffré avec l'algorithme affine

    Args:
        text (str): texte à déchiffrer
        a (int): clé a
        b (int): clé b
        
    Returns:
        str: texte déchiffré
    """
    text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for c in text: 
        if(c in alphabet): # Si le caractère est dans l'alphabet
            result += alphabet[(modulaire_inverse(a, 26) * (alphabet.index(c) - b)) % 26] # On déchiffre le caractère
        else:
            result += c
    return result

def affine_decode_all(text): 
    """ Déchiffre un texte chiffré avec l'algorithme affine en testant toutes les clés possibles 

    Args:
        text (str): texte à déchiffrer

    Returns:
        str: texte déchiffré
    """
    distance_min = distanceFreq(text)
    res =""
    for a in range(1, 26): # On teste toutes les clés possibles de a
        if(pgcd(a, 26) == 1): # Si le PGCD de a et 26 est égal à 1 
            for b in range(1, 26): # On teste toutes les clés possibles de b
                distance = distanceFreq(affine_decode(text, a, b)) # On calcule la distance entre la fréquence d'apparition des lettres dans le texte déchiffré et la fréquence d'apparition des lettres dans l'alphabet
                if distance < distance_min:
                    distance_min = distance # Si la distance est plus petite que la distance minimale, on met à jour la distance minimale
                    res = affine_decode(text, a, b) # On met à jour le résultat
    return res                   


def main():
    continuer = True
    while continuer:
        texte = input("\n\n\n         Entrez le texte à déchiffrer:      \n\n\n")
        print("\n\n\n")
        print("\n\n"+affine_decode_all(texte)+"\n\n")
        print("\n\n\n")
        
        continuer = input("Voulez-vous continuer? (O/N) ").upper() != "N"
        