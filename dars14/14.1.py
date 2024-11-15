# num1 = [12,33,56,83,49]
# num2 = []
# for i in num1:
#     x = i // 10
#     y = i % 10
#     num2.append(x+y)
#     print(num2)

# Foydalanuvchidan qatorlar soni va har bir qatordagi harflar sonini so'raymiz
qatorlar = int(input("Qatorlar sonini kiriting: "))
harflar_bir_qator = int(input("Har bir qatordagi harflar sonini kiriting: "))

# A dan Z gacha bo'lgan harflarni ro'yxatini yaratamiz
import string
harflar = string.ascii_uppercase

# Harflarni kerakli qatorlarga joylashtiramiz
index = 0  # Harflarni indekslash uchun o'zgaruvchi

for i in range(qatorlar):
    # Har bir qator uchun kerakli sonni chiqaramiz
    qator = harflar[index:index+harflar_bir_qator]
    print(qator)
    index += harflar_bir_qator  # Indeksni oshiramiz
    if index >= len(harflar):
        break  # Agar harflar tugasa, tsiklni to'xtatamiz
