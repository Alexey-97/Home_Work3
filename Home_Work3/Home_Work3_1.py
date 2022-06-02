a = int(input("Введите число  меньше 10: "))
while a > 10:
    a = int(input("Введите число ещё раз меньше 10: "))
b = int(input("Введите число  меньше или равное первому числу: "))
# print(a)
while b < a :
    b = int(input("Введите число  большее или равное первому числу: "))
c = int(input("Введите число  меньше 10: "))
while c > 10:
    c = int(input("Введите число ещё раз меньше 10: "))
d = int(input("Введите число  меньше или равное первому числу: "))
while c > d :
    d = int(input("Введите число  большее или равное первому числу: "))
print("")

numbers = []
for i in range(c,d + 1):
    numbers.append(i)
for i in numbers:
    print("\t",i ,end="\t",)
print()
for i in range(a,b + 1 ):
    for j in range(c,d + 1):
        if j == numbers[0]:
            print(i,"\t"f'{i * j}',end = "\t")
        else:
            print("\t",f'{i * j}',end = "\t")
    print()

