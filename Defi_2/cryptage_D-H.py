import math
import random

def est_premier(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True

def genere_premier(n):
    r = random.randint(0,n)
    while not (est_premier(r)):
        r = random.randint(2,n)
    return r

def cryptage(n,g):
    #Choix d'Alice
    Ka = random.randint(1,n)
    Ya = pow(g,Ka,n)
    #Choix de Bob
    Kb = random.randint(1,n)
    Yb = pow(g,Kb,n)
    # Bob envoie Ya à Alice
    y = pow(Yb,Ka,n)
    # Alice envoie Yb à Bob
    y2 = pow(Ya,Kb,n)
    return (y,y2,pow(g,Kb*Ka,n))


n = genere_premier(pow(2,20))
print(cryptage(n,5))
