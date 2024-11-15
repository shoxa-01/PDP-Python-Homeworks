# Foydalanuvchidan son kiritishni so'raymiz
number = int(input("Sonni kiriting: "))

# Sonni ikkilik sanoq tizimiga o'tkazamiz va "0b" prefiksisiz qoldiramiz
binary_number = bin(number)[2:]

# Ikkilik sonni teskari tartibda yozamiz
reversed_binary = binary_number[::-1]

# Natijani chiqaramiz
print("Asl ikkilik ko'rinish:", binary_number)
print("Teskari ikkilik ko'rinish:", reversed_binary)
