import math

def baby_giant_step(g, a, n):

    baby_step = {}
    giant_step = {}

    m = int(math.sqrt(n))
    for i in range(m):
        baby = pow(a, m*i, n)
        baby_step[i] = baby

    for j in range(m):
        giant = g * pow(a, -j, n) % n
        giant_step[j] = giant

    for kb, vb in baby_step.items():
        for kg, vg in giant_step.items():
            if vb == vg:
                return m*kb + kg % n
