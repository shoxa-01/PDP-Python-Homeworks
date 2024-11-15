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
