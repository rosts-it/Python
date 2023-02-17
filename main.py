digit = int(input())
a = digit % 10             # Позиция единиц
b = (digit % 100) // 10    # Позиция десятков

d = digit // 100           # Позиция тысяч

print('Сумма цифр =', d)
print('Произведение =', a)
print('Произведение цифр =', b)

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# sum = 3*(a+b+c+d)
# print(sum)

# my_list = [1, 2, 3]
# print(my_list)


# def my_fn():        # Мой коменнтарий
#     print('Hello')  # Мой коменнтарий


# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')

# str1 = input()
# str2 = input()
# str3 = input()
# razd = input()
# print(str1, str2, str3, sep=razd)
