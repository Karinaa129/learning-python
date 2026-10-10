# ============================================================
# Итоговая работа. Блок 4: Циклы for и while
# ============================================================
# Дата: 10.10.2026
# Статус:  сдано
# ============================================================
# Задача 1.
n = int(input())
total = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:          
        total += digit
    n //= 10

print(total)

# Задача 2.
n = 8                 # было 7
count = 0
maximum = -10**13     # было 1000 - теперь заведомо меньше любого возможного числа
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:    # было x // 4 == 0 - теперь проверка остатка
        count += 1
        if x > maximum:   # было x < maximum - теперь ищем максимум
            maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# Задача 3.
n = 4
count = 0
maximum = -10**9          # было 999
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x   # было maximum = i
                          # был break - убрали
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# Задача 4.
n = int(input())

# Первая строка - полностью из звёзд (ширина 19)
print('*' * 19)

# Средние строки: звезда в начале, пробелы внутри, звезда в конце
for _ in range(n - 2):
    print('*' + ' ' * 17 + '*')

# Последняя строка - тоже полностью из звёзд
print('*' * 19)

# Задача 5.
n = int(input())

while n > 999:
    n //= 10

print(n % 10)

# Задача 6.
n_str = input()
last_digit = n_str[-1]

print(n_str.count('3'))
print(n_str.count(last_digit))

count_even = sum(1 for d in n_str if int(d) % 2 == 0)
print(count_even)

sum_gt_5 = sum(int(d) for d in n_str if int(d) > 5)
print(sum_gt_5)

product_gt_7 = 1
for d in n_str:
    if int(d) > 7:
        product_gt_7 *= int(d)
print(product_gt_7)

print(n_str.count('0') + n_str.count('5'))



