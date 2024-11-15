# 1-masala

n = 7
k = 3
for i in range(n):
    print(k)

# 2-masala

a = 1
b = 5
count = 0
for i in range(a, b + 1):
    print(i)
    count += 1
print("Hamma sonlar:", count)

# 3-masala

a = 1
b = 5
count = 0
for i in range(b, a - 1, -1):
    if i < 5 and i > 1:
        print(i)
        count += 1
print("Hamma sonlar:", count)

# 4-masala

kanfet_kg_narxi = 7
for i in range(1, 11):
    print(i, "kg:", kanfet_kg_narxi * i)

# 5-masala

kanfet_kg_narxi = 7.5
for i in range(1, 11):
    print(i / 10, "kg:", kanfet_kg_narxi * (i / 10))

# 6-masala

kanfet_kg_narxi = 7.5
for i in range(12, 21, 2):
    print(i / 10, "kg:", kanfet_kg_narxi * (i / 10))

# 7-masala

a = 1
b = 5
summa = 0
for i in range(a, b + 1):
    summa += i
print("Yig'indisi:", summa)

# 8-masala

a = 3
b = 5
product = 1
for i in range(a, b + 1):
    product *= i
print("Ko'paytmasi:", product)

# 9-masala

a = 2
b = 5
kvadrat = 0
for i in range(a, b + 1):
    kvadrat += i ** 2
print("Kvadratlar yig'indisi:", kvadrat)

# 10-masala

n = 8
sum = 0
for i in range(1, n + 1):
    sum += 1 / i
print("Yig'indi S =", sum)

# 11-masala

n = 5
kvadrat = 0
for i in range(1, n + 1):
    kvadrat += i ** 2
print("Kvadratlar yig'indisi:", kvadrat)

# 12-masala

n = 5
product = 1
for i in range(1, n + 1):
    product *= i
print("Ko'paytma S =", product)


# 14-masala

n = 5
for i in range(1, n + 1):
    print(i, "ning kvadrati:", i ** 2)

# 15-masala

a = 2
n = 3
result = 1
for i in range(n):
    result *= a
print(a, "ning", n, "-darajasi:", result)



