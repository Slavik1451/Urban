s = input("Напиши текст ")
s1 = s
print(f"Твой текст: {s}")
print("*"*24)
print("Начинаю форматировать символы с помощью ord()")
print("*"*24)
list_ord = list()
for c in s:
    list_ord.append(ord(c))

str_ord = list(map(str, list_ord))
str_binary = list(map(bin, list_ord))
str_binary = list(map(lambda string: string.replace('0b', ''), str_binary))
print(f'Текст в Unicode: {" ".join(str_ord)}')
print(f'Текст в двоичке: {" ".join(str_binary)}')