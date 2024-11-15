# 1-masala

x = int(input("son kiriting: "))
if x > 0:
    x += 1
print(x)

# 2-masala

x = int(input("son kiriting: "))
if x > 0:
    x += 1
else:
    x -= 2
print(x)

# 3-masala

x = int(input("son kiriting: "))
if x > 0:
    x += 1
elif x < 0:
    x -= 2
else:
    x = 10
print(x)

# 4-masala

a, b, c = int(input("a qiymatni kiriting: ")), int(input("b qiymatni kiriting: ")), int(input("c qiymatni kiriting: "))
num2 = 0
if a > 0:
    num2 += 1
if b > 0:
    num2 += 1
if c > 0:
    num2 += 1
print(num2)

# 5-masala

a, b, c = int(input("a qiymatni kiriting: ")), int(input("b qiymatni kiriting: ")), int(input("Ec qiymatni kiriting: "))
num1, num2 = 0, 0
if a > 0:
    num1 += 1
elif a < 0:
    num2 += 1
if b > 0:
    num1 += 1
elif b < 0:
    num2 += 1
if c > 0:
    num1 += 1
elif c < 0:
    num2 += 1
print("num1", num1)
print("num2:", num2)

# 6-masala

a, b = int(input("a qiymatni kiriting: ")), int(input("b qiymatni kiriting: "))
if a > b:
    print(a)
else:
    print(b)

# 7-masala

a, b = int(input("a qiymatni kiriting: ")), int(input("b qiymatni kiriting: "))
if a < b:
    print("Order:", a, b)
else:
    print("Order:", b, a)

8-masala

a, b = int(input("a qiymatni kiriting: ")), int(input("b qiymatni kiriting: "))
if a > b:
    print("Larger first:", a, b)
else:
    print("Larger first:", b, a)

# 9-masala

A, B = float(input("A qiymatni kiriting: ")), float(input("B qiymatni kiriting: "))
if A > B:
    A, B = B, A
print("A:", A, "B:", B)

# 10-masala

A, B = int(input("A qiymatni kiriting: ")), int(input("B qiymatni kiriting: "))
if A != B:
    A = B = A + B
else:
    A = B = 0
print("A:", A, "B:", B)

# 11-masala

A, B = int(input("A qiymatni kiriting: ")), int(input("B qiymatni kiriting: "))
if A != B:
    if A > B:
        B = A
    else:
        A = B
else:
    A = B = 0
print("A:", A, "B:", B)

# 12-masala

a, b, c = int(input("a qiymatni kiriting: ")), int(input("b qiymatni kiriting: ")), int(input("c qiymatni kiriting: "))
print("Smallest:", min(a, b, c))

a, b, c, d = int(input("Enter integer a for if19: ")), int(input("Enter integer b: ")), int(input("Enter integer c: ")), int(input("Enter integer d: "))
if a == b == c and c != d:
    print(4)
elif a == b == d and b != c:
    print(3)
elif a == c == d and a != b:
    print(2)
elif b == c == d and a != b:
    print(1)



