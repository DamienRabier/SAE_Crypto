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

def decryptage_force_brute(n, g, ya, yb, T):
    #Trouvez Ka, la clé d'Alice
    Ka = None
    for i in range(1,pow(2,T)):
        if pow(g,i,n) == ya:
            Ka = i
            break
    if Ka is None:
        return None
    #Trouvez Kb, la clé de Bob
    Kb = None
    for i in range(1,pow(2,T)):
        if pow(g,i,n) == yb:
            Kb = i
            break
    if Kb is None:
        return None
    y = pow(g,Kb*Ka,n)
    return y



    

