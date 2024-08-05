a = 1
b = 2
c = 0
vsota = 0
while a < 4000000:
    if a % 2 == 0:
        vsota += a
    c = a + b
    a = b
    b = c
print(vsota)