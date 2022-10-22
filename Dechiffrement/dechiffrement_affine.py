ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphaMap = {"A":8.4,"B":1.05,"C":3.03,"D":4.18,"E":17.26,"F":1.12,"G":1.27,"H":0.92,"I":7.34,"J":0.31,"K":0.05,"L":6.01,"M":2.96,"N":7.13,"O":5.26,"P":3.01,"Q":0.99,"R":6.55,"S":5.08,"T":7.07,"U":5.74,"V":1.32,"W":0.04,"X":0.45,"Y":0.30,"Z":0.12}
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def enlever_caractere_non_dico(texte):
    texte = texte.upper()
    for mot in texte:
        if mot not in ALPHABET:
            texte = texte.replace(mot, "")
    return texte

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
    
def pgcd(a, b):
    if(b == 0):
        return a
    else:
        return pgcd(b, a % b)

def modulaire_inverse(a, n):
    for i in range(1, n):
        if((a * i) % n == 1):
            return i
    return 1

def affine_decode(text, a, b):
    text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for c in text:
        if(c in alphabet):
            result += alphabet[(modulaire_inverse(a, 26) * (alphabet.index(c) - b)) % 26]
        else:
            result += c
    return result

def affine_decode_all(text):
    distance_min = distanceFreq(text)
    res =""
    for a in range(1, 26):
        if(pgcd(a, 26) == 1):
            for b in range(1, 26):
                distance = distanceFreq(affine_decode(text, a, b))
                if distance < distance_min:
                    distance_min = distance
                    res = affine_decode(text, a, b)
    return res                   