word = input("""Введите текст:
""").lower()
word = word.split()
my_list = list()
for item in word:
      if item not in my_list:
            my_list.append(item)
a = 0
for i in my_list:
      for j in word:
            if i == j:
                  a += 1
      print(i,a )
      a = 0


