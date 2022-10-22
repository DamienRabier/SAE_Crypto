from dis import dis


chiffre = "Dwi gsftn seebvzx ezjg jzzo. Zp ldvzx npvlh. Tt jlzcqo jsy dvjmdbvj, wnzpke wi ilme. Qg wetavzx owpo. Yy jmlme qiumdbdege ujexlqo uy qipssfzb. Lr nimzpwwi, gpfa gfycl ll'yy ogrw, atpj wzcmu uf'ci ksnade, twcn gvznjeh bc'pe fzcmusy, vje pzqi, jsyvv kvzqn tsfxn. Uy niirp Didex-Ximkmy, ci tplxjkmd xgrmybdw wtoirplqo lr npvceyl llm ainjetb."
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphaMap = {"A":8.4,"B":1.05,"C":3.03,"D":4.18,"E":17.26,"F":1.12,"G":1.27,"H":0.92,"I":7.34,"J":0.31,"K":0.05,"L":6.01,"M":2.96,"N":7.13,"O":5.26,"P":3.01,"Q":0.99,"R":6.55,"S":5.08,"T":7.07,"U":5.74,"V":1.32,"W":0.04,"X":0.45,"Y":0.30,"Z":0.12}
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Décryptage de vigenere
def vigenere_inverse(texte,cle):
    """Décryptage de vigenere"""
    texte = texte.upper()
    cle = cle.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultat = ""
    i_cle = 0
    for i in range(len(texte)):
        if texte[i] in alphabet:
            if i_cle == len(cle):
                i_cle = 0
            resultat += alphabet[(alphabet.index(texte[i]) - alphabet.index(cle[i_cle % len(cle)])) % len(alphabet)]
            i_cle += 1
        else:
            resultat += texte[i]
    return resultat

def enlever_caractere_non_dico(texte):
    texte = texte.upper()
    for mot in texte:
        if mot not in ALPHABET:
            texte = texte.replace(mot, "")
    return texte
    
def indice_de_coincidence(texte):
    """Calcule l'indice de coincidence d'un texte"""
    texte = enlever_caractere_non_dico(texte)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultat = 0
    for lettre in alphabet:
        resultat += texte.count(lettre) * (texte.count(lettre) - 1)
    return resultat / (len(texte) * (len(texte) - 1))



def texte_par_portion(texte,portion):
    """Decoupe un texte en plusieurs portions"""
    texte = enlever_caractere_non_dico(texte)
    resultat = []
    for i in range(portion):
        resultat.append("")
    for i in range(len(texte)):
        resultat[i % portion] += texte[i]
    return resultat

def longueur_cle(texte):
    for i in range(1,20):
        decoupe = texte_par_portion(texte,i)
        somme_ic=0
        for elem in decoupe:
            somme_ic += indice_de_coincidence(elem)
        moyenne_ic = somme_ic/len(decoupe)
        if 0.065 < moyenne_ic < 0.08:
            return i
    return 0

def dic_freq(texte):
    dic = {}
    texte = enlever_caractere_non_dico(texte)
    for lettre in alpha:
        dic[lettre] = 0
    
    for lettre in texte:
        if lettre in alpha:
            dic[lettre] += 1
    for lettre in dic:
        dic[lettre] = dic[lettre]/len(texte)*100
    return dic
    
def distanceFreq(texte):
    freq = dic_freq(texte)
    distance = 0
    for lettre in alpha:
        distance += abs(freq[lettre] - alphaMap[lettre])
    return distance

def decal(chaine,decalage):
    chaine = enlever_caractere_non_dico(chaine)
    
    resultat = ""
    for lettre in chaine:
        if lettre.isalpha():
            resultat += chr((ord(lettre) - ord("A") + decalage) % 26 + ord("A"))
        else:
            resultat += lettre
    return resultat


def decodage_freq_decryptage(texte):
    d_mini = distanceFreq(texte)
    decalage = 0
    for d in range(1,26):
        nv_text = decal(texte,d)
        if d_mini > distanceFreq(nv_text):
            d_mini = distanceFreq(nv_text)
            decalage = d
    return ((26 - decalage) % 26)

        
def recherche_mot_cle(chaine,longueur):
    mot = ''
    liste_decomp = texte_par_portion(chaine,longueur)
    
    for liste in liste_decomp:
        str_chaine = ''.join(str(elem) for elem in liste)
        lettre = decodage_freq_decryptage(str_chaine)
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
        