n = 1
vsota = 0
while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        vsota += n
    n += 1    
print(vsota)
    