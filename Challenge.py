min = int(input("Masukkan angka minimum: "))
max = int(input("Masukkan angka maksimum: "))
prima = []
komposit = {}

for x in range(min, max + 1):
    if x > 1:
        is_prime = True
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                is_prime = False
                komposit[x] = None  
                # break
        if is_prime:
            prima.append(x)

print("Bilangan Prima:")
print(prima)

print("Bilangan Komposit:")
print(list(komposit.keys()))