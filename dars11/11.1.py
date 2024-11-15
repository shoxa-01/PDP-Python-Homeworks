# 1-masala
#
# qadam = 1
# while qadam < 10:
#     print(qadam)
#     qadam += 1
#
# 2-masala
#
# start = int(input("1-raqamni kiriting: "))
# stop = int(input("2-raqamni kiriting: "))
# while start <= stop:
#     print(start)
#     start += 1
#
# 3-masala
# start = int(input("1-raqamni kiriting: "))
# # stop = int(input("2-raqamni kiriting: "))
# #
# # if start > stop:
# #     temp = stop
# #
# # while start <= stop:

n = int(input("Xonalar sonini kiriting: "))

start = 10**(n-1)
end = 10**n - 1
i = start

while i <= end:
    print(i)
    i += 1