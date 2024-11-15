# 1-masala

car = float(input("Avtomobilning narxini kiriting: "))
tolangan = float(input("To'langan qismini kiriting: "))
oy = int(input("Necha oyga bo'lib to'lashni xohlaysiz?: "))
yillik_foiz = float(input("Yillik foiz miqdorini kiriting: "))

if tolangan >= car * 0.5:
    qolgan_sum = car - tolangan
    oylik_tolov = qolgan_sum // oy
    oshirilgan_qolgan_sum = qolgan_sum * (1 + yillik_foiz / 100)
    oylik_foiz_tolov = oshirilgan_qolgan_sum // oy

    print(f"Qolgan qismini {oy} oyga bo'lib to'lash uchun oylik to'lov miqdori: {oylik_tolov} so'm")
    print(f"Yillik {yillik_foiz}% oshirish bilan oylik to'lov miqdori: {oylik_foiz_tolov} so'm")
else:
    print("To'lov umumiy narxning kamida 50% bo'lishi kerak!")

# 1 - masala
yosh = int(input("Yoshingizni kiriting: "))
if yosh >= 18:
    print("voyaga yetgan")
else:
    print("voyaga yetmagan")

# 2 - masala
baho = int(input("Bahoni kiriting: "))
if baho == 5:
    print("a'lo")
elif baho == 4:
    print("yaxshi")
elif baho == 3:
    print("qoniqarli")
elif baho == 2:
    print("qoniqarsiz")

# 3 - masala
oy = int(input("Oy raqamini kiriting: "))
if oy in [12, 1, 2]:
    print("Qish fasli")
elif oy in [3, 4, 5]:
    print("Bahor fasli")
elif oy in [6, 7, 8]:
    print("Yoz fasli")
elif oy in [9, 10, 11]:
    print("Kuz fasli")

# 4 - masala
harorat = float(input("Havoning haroratini kiriting: "))
if harorat > 30:
    print("havo issiq")
elif 20 <= harorat <= 30:
    print("havo iliq")
elif harorat < 15:
    print("havo sovuq")

# 5 - masala
kun = int(input("Hujjat amal qilish muddati (kun): "))
if kun > 5:
    print("hujjat amal qilish muddati tugadi")
else:
    print("hujjat amal qilish muddati hali tugamagan")

# 6 - masala
tolov_usuli = input("To'lov usulini kiriting (naqt yoki karta): ")
if tolov_usuli == "naqt":
    summa = float(input("Summani kiriting: "))
    print("Summa kiritildi:", summa)
elif tolov_usuli == "karta":
    parol = input("Parolni kiriting: ")
    print("Parol qabul qilindi")

# 7 - masala
baho = int(input("Bahoni kiriting: "))
if baho >= 90:
    print("A")
elif baho >= 80:
    print("B")
elif baho >= 70:
    print("C")
elif baho >= 60:
    print("D")
else:
    print("F")

# 8 - masala
yosh = int(input("Yoshingizni kiriting: "))
if yosh > 18:
    print("Kattalar")
else:
    print("Bolalar")

# 9 - masala
ob_havo = input("Ob-havo qanday? (yomg'ir/qor/yaxshi): ")
if ob_havo == "yomg'ir" or ob_havo == "qor":
    print("Ko'ylak kiyma")

# 10 - masala
tolov_turi = input("To'lov turini tanlang (naqd yoki kartochka): ")
if tolov_turi == "naqd":
    print("Siz naqd to'lovni tanladingiz")
elif tolov_turi == "kartochka":
    print("Siz kartochka orqali to'lovni tanladingiz")
