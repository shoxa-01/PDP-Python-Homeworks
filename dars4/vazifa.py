# amount = int(input("Qancha pulingiz bor? So'mda kiriting: "))
# distance = int(input("Masofani km bo'yicha kiriting: "))
# taxi = int(input("Taksi narxini km bo'yicha so'mda kiriting: "))
# bus = int(input("Avtobus narxini so'mda kiriting: "))
# station = int(input("Bekatlar sonini kiriting: "))
#
# check_taxi = distance * taxi <= amount
# check_bus = station * bus <= amount
#
# print("\nTaksida ketish mumkinligi:", check_taxi)
# print("Avtobusda ketish mumkinligi:", check_bus)


# amound = int(input("Qancha pulingiz bor: "))
# distance = int(input("Masofani km tarzida kirgazing!: "))
# train = int(input("Poyezd narxini km bo'yicha so'mda kirgazing!: "))
# bus = int(input("Avtobus narxini km bo'yicha so'mda kirgazing: " ))
# station = int(input("Bekatlar sonini kiriting: "))
#
# check_train = distance * train <= amount
# check_bus = station * bus <= amount
# print("Poyezdda ketish mumkinligi:", check_train)
# print("Avtobusda ketish mumkinligi:", check_bus)

amount = int(input("Qancha pulingiz bor: "))
distance = int(input("Masofani km tarzida kirgazing!: "))
train = int(input("Poyezd narxini km bo'yicha so'mda kirgazing!: "))
bus = int(input("Avtobus narxini so'mda kirgazing: "))
station = int(input("Bekatlar sonini kiriting: "))

check_train = distance * train <= amount
check_bus = station * bus <= amount
print("Poyezdda ketish mumkinligi:", check_train)
print("Avtobusda ketish mumkinligi:", check_bus)
