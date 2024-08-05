def largest_prime_factor(n):
    m = 2
    seznam = []
    while m <= n:
        if n % m == 0: # če m deli n
            seznam.append(m) # ga dodamo v seznam
            n /= m # zanimajo nas še prafaktorji od preostanka števila, 
                   # ko ga že delimo s prvim prafaktorjem
            while n % m == 0:
                n /= m # če je npr. število deljivo z 2, nas ne zanimajo 
                       # več preostali faktorji 2, zato zdelimo z m, 
                       # dokler gre
        m += 1
    return seznam[-1] # v seznamu so vsa praštevila, ki delijo n, vsako
                      # pa je napisano le enkrat. Zanima nas zadnje
                      # število iz seznama, saj je to največje

print(largest_prime_factor(600851475143))