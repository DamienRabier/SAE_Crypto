
chiffre = "Dwi gsftn seebvzx ezjg jzzo. Zp ldvzx npvlh. Tt jlzcqo jsy dvjmdbvj, wnzpke wi ilme. Qg wetavzx owpo. Yy jmlme qiumdbdege ujexlqo uy qipssfzb. Lr nimzpwwi, gpfa gfycl ll'yy ogrw, atpj wzcmu uf'ci ksnade, twcn gvznjeh bc'pe fzcmusy, vje pzqi, jsyvv kvzqn tsfxn. Uy niirp Didex-Ximkmy, ci tplxjkmd xgrmybdw wtoirplqo lr npvceyl llm ainjetb."
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphaMap = {"A":8.4,"B":1.05,"C":3.03,"D":4.18,"E":17.26,"F":1.12,"G":1.27,"H":0.92,"I":7.34,"J":0.31,"K":0.05,"L":6.01,"M":2.96,"N":7.13,"O":5.26,"P":3.01,"Q":0.99,"R":6.55,"S":5.08,"T":7.07,"U":5.74,"V":1.32,"W":0.04,"X":0.45,"Y":0.30,"Z":0.12}
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Décryptage de vigenere
def vigenere_inverse(texte,cle):
    """Fonction qui permet de décrypter un texte chiffré avec la méthode de Vigenère

    Args:
        texte (String): Texte à décrypter
        cle (String): Clé de décryptage

    Returns:
        String: Texte décrypté
    """
    texte = texte.upper() # On met le texte en majuscule
    cle = cle.upper() # On met la clé en majuscule 
    resultat = "" # On initialise la variable qui contiendra le résultat
    i_cle = 0 # On initialise un compteur pour la clé
    for i in range(len(texte)): # On parcourt le texte
        if texte[i] in ALPHABET: # Si le caractère est dans l'alphabet
            if i_cle == len(cle): # Si le compteur de la clé est égal à la longueur de la clé
                i_cle = 0 # On remet le compteur à 0 
            resultat += ALPHABET[(ALPHABET.index(texte[i]) - ALPHABET.index(cle[i_cle % len(cle)])) % len(ALPHABET)] # On ajoute le caractère décalé à la clé au résultat
            i_cle += 1  # On incrémente le compteur de la clé
        else: 
            resultat += texte[i] # Si le caractère n'est pas dans l'alphabet, on l'ajoute au résultat
    return resultat 

def enlever_caractere_non_dico(texte):
    """Fonction qui permet d'enlever les caractères non présents dans l'alphabet

    Args:
        texte (String): Texte à traiter

    Returns:
        String : Texte sans caractères non présents dans l'alphabet
    """
    texte = texte.upper()
    for mot in texte: 
        if mot not in ALPHABET: 
            texte = texte.replace(mot, "") # On remplace les caractères non présents dans l'alphabet par des espaces
    return texte 
    
def indice_de_coincidence(texte):
    """Fonction qui permet de calculer l'indice de coincidence d'un texte

    Args:
        texte (String):  Texte à traiter

    Returns:
        int : Indice de coincidence du texte 
    """
    texte = enlever_caractere_non_dico(texte) # On enlève les caractères non présents dans l'alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultat = 0
    for lettre in alphabet: 
        resultat += texte.count(lettre) * (texte.count(lettre) - 1) # On calcule l'indice de coincidence du texte 
    return resultat / (len(texte) * (len(texte) - 1))



def texte_par_portion(texte,portion):
    """ Fonction qui permet de découper un texte en plusieurs parties

    Args:
        texte (String): Texte à découper
        portion (int): Nombre de parties dans lesquelles on découpe le texte

    Returns:
        list: Liste contenant les parties du texte
    """
    texte = enlever_caractere_non_dico(texte)
    resultat = []
    for i in range(portion): # On parcourt le nombre de parties
        resultat.append("") # On ajoute une partie au résultat
    for i in range(len(texte)): # On parcourt le texte
        resultat[i % portion] += texte[i] # On ajoute le caractère à la partie correspondante
    return resultat

def longueur_cle(texte):
    """Fonction qui permet de calculer la longueur de la clé

    Args:
        texte (String): Texte à traiter

    Returns:
        int: Longueur de la clé
    """
    for i in range(1,20):
        decoupe = texte_par_portion(texte,i) # On découpe le texte en i parties
        somme_ic=0
        for elem in decoupe: 
            somme_ic += indice_de_coincidence(elem) # On calcule l'indice de coincidence de chaque partie
        moyenne_ic = somme_ic/len(decoupe) # On calcule la moyenne des indices de coincidence
        if 0.065 < moyenne_ic < 0.08: 
            return i # Si la moyenne des indices de coincidence est comprise entre 0.065 et 0.08, on renvoie la longueur de la clé
    return 0

def dic_freq(texte):
    """Fonction qui permet de calculer la fréquence d'apparition des lettres dans un texte

    Args:
        texte (String): Texte à traiter
        
    Returns:
        dict: Dictionnaire contenant la fréquence d'apparition des lettres dans le texte
    """
    dic = {}
    texte = enlever_caractere_non_dico(texte) # On enlève les caractères non présents dans l'alphabet
    for lettre in alpha:
        dic[lettre] = 0 # On initialise le dictionnaire avec des valeurs à 0
    
    for lettre in texte:
        if lettre in alpha:
            dic[lettre] += 1 # On incrémente la valeur de la lettre dans le dictionnaire
    for lettre in dic:
        dic[lettre] = dic[lettre]/len(texte)*100 # On calcule la fréquence d'apparition des lettres dans le texte
    return dic 
    
def distanceFreq(texte):
    """Fonction qui permet de calculer la distance entre la fréquence d'apparition des lettres dans un texte et la fréquence d'apparition des lettres dans la langue française

    Args:
        texte (String): Texte à traiter

    Returns:
        dict: Dictionnaire contenant la distance entre la fréquence d'apparition des lettres dans le texte et la fréquence d'apparition des lettres dans la langue française
    """
    freq = dic_freq(texte) # On calcule la fréquence d'apparition des lettres dans le texte
    distance = 0
    for lettre in alpha:
        distance += abs(freq[lettre] - alphaMap[lettre]) # On calcule la distance entre la fréquence d'apparition des lettres dans le texte et la fréquence d'apparition des lettres dans la langue française
    return distance

def decal(chaine,decalage):
    """Fonction qui permet de décaler une chaîne de caractères

    Args:
        chaine (String): Chaîne de caractères à décaler
        decalage (int): Décalage à appliquer 

    Returns:
        String : Chaîne de caractères décalée
    """
    chaine = enlever_caractere_non_dico(chaine)
    
    resultat = ""
    for lettre in chaine:
        if lettre.isalpha(): # On vérifie que la lettre est bien dans l'alphabet
            resultat += chr((ord(lettre) - ord("A") + decalage) % 26 + ord("A")) # On décale la lettre
        else:
            resultat += lettre
    return resultat


def decodage_freq_decryptage(texte):
    """Fonction qui permet de décoder un texte en utilisant la fréquence d'apparition des lettres dans la langue française

    Args:
        texte (String): Texte à décoder

    Returns:
        String : Texte décodé
    """
    d_mini = distanceFreq(texte)
    decalage = 0
    for d in range(1,26): # On parcourt les 26 décalages possibles
        nv_text = decal(texte,d) # On décale le texte
        if d_mini > distanceFreq(nv_text):
            d_mini = distanceFreq(nv_text) # On met à jour la distance minimale
            decalage = d # On met à jour le décalage 
    return ((26 - decalage) % 26) # On renvoie le décalage à appliquer pour décoder le texte

        
def recherche_mot_cle(chaine,longueur):
    """Fonction qui permet de rechercher le mot clé d'une chaîne de caractères

    Args:
        chaine (String): Chaîne de caractères à traiter
        longueur (int) : Longueur du mot clé

    Returns:
        String : Mot clé
    """
    mot = ''
    liste_decomp = texte_par_portion(chaine,longueur)
    
    for liste in liste_decomp:
        str_chaine = ''.join(str(elem) for elem in liste) # On transforme la liste en chaîne de caractères
        lettre = decodage_freq_decryptage(str_chaine) # On décode la chaîne de caractères
        mot += alpha[lettre]
    return mot


def main():
    continuer = True
    while continuer:
        texte = input("\n\n\n         Entrez le texte à déchiffrer:      \n\n\n")
        print("\n\n\n")
        print(vigenere_inverse(texte,recherche_mot_cle(texte,longueur_cle(texte))))
        print("\n\n\n")
        
        continuer = input("Voulez-vous continuer? (O/N) ").upper() != "N"
    
if __name__ == "__main__":
    main()
        