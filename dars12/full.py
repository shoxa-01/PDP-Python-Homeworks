# Dastlabki qiymat
money = 100
# Maqsad qiymat
target = 200
# Oylik daromad foizi
rate = 0.1
# Oylarni hisoblash uchun o'zgaruvchi
months = 0

# Maqsadga yetguncha davom etadi
while money < target:
    money += money * rate  # Har oy pul 0.1 foizga ko'payadi
    months += 1            # Oylik hisoblagichni oshiramiz

print("200$ olish uchun oylar soni:", months)
