def sum_square_difference(n=100):
    vsota_kvadratov = 0
    vsota = 0
    for i in range(n + 1):
        vsota_kvadratov += i ** 2
        vsota += i
    return abs(vsota_kvadratov - vsota ** 2)

print(sum_square_difference())