def je_prastevilo(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def katero_je(prastevilo):
    seznam = []
    i = 2
    while len(seznam) < prastevilo:
        if je_prastevilo(i):
            seznam.append(i)
        i += 1
    return seznam[-1]

print(katero_je(10001))