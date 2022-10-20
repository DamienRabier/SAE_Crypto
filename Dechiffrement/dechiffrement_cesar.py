from cmath import sqrt
import string



texte_chiffre = "Zc krgfkr u'le ufzxk le rzi drikzrc jli c'fscfex tyrjjzj ul mrjzjkrj.Zc flmizk jfe wizxf dlirc, zc gizk ul crzk wifzu, zc slk le xireu sfc. Zc j'rgrzjrzk. Zc j'rjjzk jli jfe tfjp, zc gizk le aflierc hl'zc gritflilk u'le rzi uzjkirzk. Zc rccldr le tzxrizccf hl'zc wldr aljhl'rl sflk hlfzhl'zc kiflmrk jfe griwld ziizkrek. Zc kfljjr."
alphaMap = {"A":8.4,"B":1.05,"C":3.03,"D":4.18,"E":17.26,"F":1.12,"G":1.27,"H":0.92,"I":7.34,"J":0.31,"K":0.05,"L":6.01,"M":2.96,"N":7.13,"O":5.26,"P":3.01,"Q":0.99,"R":6.55,"S":5.08,"T":7.07,"U":5.74,"V":1.32,"W":0.04,"X":0.45,"Y":0.30,"Z":0.12}
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def dic_freq(texte):
    dic = {}
    texte = texte.upper()
    for lettre in alpha:
        dic[lettre] = 0
    
    for lettre in texte:
        if lettre in alpha:
            dic[lettre] += 1
    for lettre in dic:
        dic[lettre] = dic[lettre]/len(texte)*100
    return dic
    
def distanceFreq(texte:string):
    freq = dic_freq(texte)
    distance = 0
    for lettre in alpha:
        distance += abs(freq[lettre] - alphaMap[lettre])
    return distance


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
    distance_min = distanceFreq(texte_chiffre)
    decal_min = 0
    for indice_decal in range(1,26):
        res = dechiffrement_cle_decalage(texte_chiffre,indice_decal)
        distance = distanceFreq(res)
        if distance < distance_min:
            distance_min = distance
            decal_min = indice_decal
    return dechiffrement_cle_decalage(texte_chiffre,decal_min%26)


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
        
        
