def largest_palindrome_product(n, m):
    najvecji = 0
    for i in range(n, m + 1): #vključno z n in brez m+1, torej do vključno m
        for j in range(n, i + 1):
            produkt = i * j
            if str(produkt) == str(produkt)[::-1] and produkt > najvecji: # prvi pogoj preveri, ali je palindrom
                najvecji = produkt
    
    return najvecji

print(largest_palindrome_product(100, 999))