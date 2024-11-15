# gentra = 15000
# cobalt = 14000
# nexia3 = 10000
# spark = 9000
# summa = int(input("Summa kiriting : "))
# check = summa >= gentra
# print("pulingiz gentraga yetadimi: ", check)
# check = summa >= cobalt
# print("pulingiz cobalt yetadimi: ", check)
# check = summa >= nexia3
# print("pulingiz nexia3 yetadimi: ", check)
# check = summa >= spark
# print("pulingiz spark yetadimi: ", check)


gentra = 15000
cobalt = 14000
nexia3 = 10000
spark = 9000
summa = int(input("Summa kiriting : "))
sum = summa - gentra
check = summa >= gentra
print(f"Gentra xarid qilganingizdan so'ng sizdagi qolgan mablag': {sum}")
print("pulingiz gentraga yetadimi: ", check)
sum = summa - cobalt
check = summa >= cobalt
print(f"Cobalt xarid qilganingizdan so'ng sizdagi qolgan mablag': {sum}")
print("pulingiz cobaltga yetadimi: ", check)
sum = summa - nexia3
check = summa >= nexia3
print(f"Nexia3 xarid qilganingizdan so'ng sizdagi qolgan mablag': {sum}")
print("pulingiz nexia3ga yetadimi: ", check)
sum = summa - spark
check = summa >= spark
print(f"Spark xarid qilganingizdan so'ng sizdagi qolgan mablag': {sum}")
print("pulingiz sparkga yetadimi: ", check)


