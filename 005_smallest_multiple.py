def smallest_multiple(n=1, m=20):
    stevilo = m
    ali_je_ok = True
    while stevilo < m ** m:
        for i in range(n, m + 1): # gremo čez vsa števila v tistem 
                                  # rangeu, ki smo ga podali na začetku
            if stevilo % i != 0:
                ali_je_ok = False
                break
            else:
                continue
        if ali_je_ok == True:
            return stevilo
        else:
            stevilo += m
            ali_je_ok = True
    return None
print(smallest_multiple(1,20))