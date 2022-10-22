import unidecode
import math
import numpy as np
import dechiffrement_cesar
import dechiffrement_vigenere

texte_a_dechiffrer = "Sop u'dffrmtfe oz qvigpjcm, bh nnaqhd iw hcbvrl dvercy, h d'youcxlmdc zpzirn, ay eg xpzzht, qy eg xohirgxpb, ymsu lstlhf bh zhkhakc, z'lbnnecvz, layoanfe bh bidv g'dlky. Oy x'txdwiyoh, gnvxnnt w'txwlkhr g'bh uuhr oju, nyor v'nnaqhd dwvz akl ojr, erdpzhyomennv innr vn nmim tqvfe om'xl yof qv x'cmksxluzf."
texte_a_chiffrer = "Sur l'abattant du vasistas, un animal au thorax indigo, à l'aiguillon safran, ni un cafard, ni un charançon, mais plutôt un artison, s'avançait, traînant un brin d'alfa. Il s'approcha, voulant l'aplatir d'un coup vif, mais l'animal prit son vol, disparaissant dans la nuit avant qu'il ait pu l'assaillir."
alphabet_min = "abcdefghijklmnopqrstuvwxyz"
dico_alphabet_chiffre = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7, "i" : 8, "j" : 9, "k" : 10, "l" : 11, "m" : 12, "n" : 13, "o" : 14, "p" : 15, "q" : 16, "r" : 17, "s" : 18, "t" : 19, "u" : 20, "v" : 21, "w" : 22, "x" : 23, "y" : 24, "z" : 25}
dico_chiffre_alphabet = {0 : "a", 1 : "b", 2 : "c", 3 : "d", 4 : "e", 5 : "f", 6 : "g", 7 : "h", 8 : "i", 9 : "j", 10 : "k", 11 : "l", 12 : "m", 13 : "n", 14 : "o", 15 : "p", 16 : "q", 17 : "r", 18 : "s", 19 : "t", 20 : "u", 21 : "v", 22 : "w", 23 : "x", 24 : "y", 25 : "z"}
alphaMap = {"A":8.4,"B":1.05,"C":3.03,"D":4.18,"E":17.26,"F":1.12,"G":1.27,"H":0.92,"I":7.34,"J":0.31,"K":0.05,"L":6.01,"M":2.96,"N":7.13,"O":5.26,"P":3.01,"Q":0.99,"R":6.55,"S":5.08,"T":7.07,"U":5.74,"V":1.32,"W":0.04,"X":0.45,"Y":0.30,"Z":0.12}
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


#retire les caractères non alphabetique et stock ce caractère avec sa position pour le replcacer
def retire_recup_caracter_non_alpha(texte):
    texte_min = unidecode.unidecode(texte).lower()
    liste = []
    for ind in range(len(texte_min)):
        if texte_min[ind] not in alphabet_min:
            liste.append((texte_min[ind], ind))
            texte = texte.replace(texte_min[ind], "")
            ind -= 1
    
    return (texte, liste)


#replace les caractères non alphabétiques
def replace_carac_non_alpha(texte, liste_replace):
    for (carac, ind) in liste_replace:
        texte = texte[:ind] + carac + texte[ind:]
    return texte
        

#calcule le pgcd
def pgcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = pgcd(b % a, a)
        return (g, x - (b // a) * y, y)


#calcule l'inverse modulaire d'un nombre
def inverse_modulaire_nombre(nb, mod):
    g, x, y = pgcd(nb, mod)
    if g != 1:
        return 'inverse modulaire inexistant'
    else:
        return x % mod


#multipli 2 matrice
def multipli_matrice(matrice1, matrice2):
    m1 = np.array(matrice1)
    m2 = np.array(matrice2)
    return m1@m2


#calcule le determinant d'une matrice
def determinant_matrice(matrice):
    return round(np.linalg.det(matrice))


#cryptage de Hill
def crypt_hill(texte, mat_cle):
    texte_min, liste_replace = retire_recup_caracter_non_alpha(texte)
    texte_min = unidecode.unidecode(texte_min).lower()
    matrices_texte = []
    pair = len(texte_min)%2 == 0
    if pair:
        for ind in range(0, len(texte_min), 2):
            matrices_texte.append([[dico_alphabet_chiffre[texte_min[ind]]], [dico_alphabet_chiffre[texte_min[ind+1]]]])
    else:
        for ind in range(0, len(texte_min)-1, 2):
            matrices_texte.append([[dico_alphabet_chiffre[texte_min[ind]]], [dico_alphabet_chiffre[texte_min[ind+1]]]])
        matrices_texte.append([[dico_alphabet_chiffre[texte_min[-1]]], [0]])

    matrices_texte_crypt = []
    for matrice_t in matrices_texte:
        matrices_texte_crypt.append(multipli_matrice_modulo26(mat_cle, matrice_t))
    
    texte_crypt = ""
    for matrice_t_c in matrices_texte_crypt:
        texte_crypt = texte_crypt + dico_chiffre_alphabet[matrice_t_c[0][0]] + dico_chiffre_alphabet[matrice_t_c[1][0]]
        
    if not pair:
        texte_crypt = texte_crypt[0:len(texte_crypt)-1]

    texte_crypt = replace_carac_non_alpha(texte_crypt, liste_replace)    

    return texte_crypt  


#décrypte Hill
def decrypt_hill(texte):
    meilleur_decode = ""
    meilleur_distance = None
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    mat_decode = [[a, b], [c, d]]
                    g, x, y = pgcd(26, determinant_matrice(mat_decode))
                    if g == 1:
                        decode = crypt_hill(texte, mat_decode)
                        distance = dechiffrement_vigenere.distanceFreq(decode)
                        print(meilleur_distance)
                        if meilleur_distance is None:
                            meilleur_distance = distance
                            meilleur_decode = decode
                        else:
                            if meilleur_distance > distance:
                                meilleur_distance = distance
                                meilleur_decode = decode
    return meilleur_decode


#calcule l'inverse d'une matrice
def inverse_matrice(matrice):
    mat_inv = np.linalg.inv(matrice)
    return mat_inv


#calcule une matrice modulo m
def matrice_modulo_26(matrice):
    for ind_ligne in range(len(matrice)):
        for ind_colonne in range(len(matrice[ind_ligne])):
            matrice[ind_ligne][ind_colonne] = matrice[ind_ligne][ind_colonne]%26
    return matrice

#calcule l'inverse d'une matrice modulo 26
def inverse_martice_modulo(matrice):
    return matrice_modulo_26(inverse_matrice(matrice))

#multiplie 2 matrices et applique le modulo 26
def multipli_matrice_modulo26(matrice1, matrice2):
    return matrice_modulo_26(multipli_matrice(matrice1, matrice2))
    

mat1 = [[2,3],[5,7]]
mat2 = [[3], [2]]

#print(crypt_hill(texte_a_chiffrer, [[2,3],[5,7]]))
print(decrypt_hill(texte_a_dechiffrer))

    

#Déchiffrement de hill

#trouver matrice chiffrement

#inverse matrice de chiffrement 
#la multiplier (modulo 26) par un inverse modulaire du déterminant de A