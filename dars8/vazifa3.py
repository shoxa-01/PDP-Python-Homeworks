year = int(input("Yilni kiriting: "))

check = year % 100 != 0 and year % 4 == 0 or year % 400 == 0

print(check)