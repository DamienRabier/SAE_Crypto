import random


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

print(cryptage(pow(2,50),5))