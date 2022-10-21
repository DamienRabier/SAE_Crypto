text_a_decoder_1 = "Huyzu Izxk u'hoovihvy eht h wzopvo. Vk hkkdph. Tzu Ahc phojdhvy pvudvy ivuly. Vk ezdtth du eozgzuw tzdevo, t'httvy whut tzu kvy, t'heedxhuy tdo tzu ezkzrqzu. Vk eovy du ozphu, vk k'zdiovy, vk kdy; phvt vk u'x thvtvtthvy jd'du vpmozlkvz rzugdt, vk mdyhvy h yzdy vutyhuy tdo du pzy wzuy vk vluzohvy kh tvluvgvrhyvzu. Vk hmhuwzuuh tzu ozphu tdo tzu kvy. Vk hkkh h tzu khihmz; vk pzdvkkh du lhuy jd'vk ehtth tdo tzu gozuy, tdo tzu rzd."
with open("Utilitaires/francais.txt", encoding="utf-8") as file:
        words = set(line.strip() for line in file)

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

def compter_nb_mots_francais(liste_de_mots):
    nb_mots = 0
    for mots in liste_de_mots:
        mot = str.lower(mots)
        if mot in words:
            nb_mots+= 1
    return nb_mots

def pgcd(a, b):
    if(b == 0):
        return a
    else:
        return pgcd(b, a % b)

def modinv(a):
    for x in range(1,26):
        if((a%26)*(x%26) % 26==1):
            return x
    return "l'inverse modulaire n'existe pas"

def decoder_affine(texte,a,b):
    if modinv(a) != "l'inverse modulaire n'existe pas":
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        texte_decode = ""
        for lettre in texte:
            if str.lower(lettre) in alphabet:
                    indice_nb_lettre = ((modinv(a)*(alphabet.index(str.lower(lettre))-b))%26) % 26
                    texte_decode += alphabet[indice_nb_lettre]
                
            else:
                texte_decode += lettre
    return texte_decode

def clé_affine(texte):
    a = 1
    b = 0
    a_neg = -1
    b_neg = 0
    texte_a_decode = texte
    texte_a_decode_neg = texte
    while(compter_nb_mots_francais(separer_mots(texte_a_decode),"Utilitaires/francais.txt") < (len(separer_mots(texte_a_decode)) / 3) and (compter_nb_mots_francais(separer_mots(texte_a_decode_neg),"Utilitaires/francais.txt") < (len(separer_mots(texte_a_decode_neg)) / 3))):
        if b >= 25:
            a += 1
            while modinv(a) == "l'inverse modulaire n'existe pas":
                a += 1
            b = 0
        if b_neg <= -25:
            a_neg -= 1
            while modinv(a_neg) == "l'inverse modulaire n'existe pas":
                a_neg -= 1
            b_neg = 0
        b = b + 1
        b_neg = b_neg - 1
        texte_a_decode = decoder_affine(texte,a,b)
        texte_a_decode_neg = decoder_affine(texte,a_neg,b_neg)
    if compter_nb_mots_francais(separer_mots(texte_a_decode),"Utilitaires/francais.txt") > (len(separer_mots(texte_a_decode)) / 3):
        return (a,b)
    if compter_nb_mots_francais(separer_mots(texte_a_decode_neg),"Utilitaires/francais.txt") > (len(separer_mots(texte_a_decode_neg)) / 3):
        return (a_neg,b_neg)
    
print(a := clé_affine(text_a_decoder_1))
print(decoder_affine(text_a_decoder_1,a[0],a[1]))