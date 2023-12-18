import math, string, random

# Характеристика 
P = 10**-4
V = 3
T = 15 * 24 * 60

#Вычисление нижней границы по формуле (2)
S_star = math.ceil((V * T) / P)

#Задание мощности алфавита
alphabep = string.ascii_letters + string.digits # Используем английский алфавит
A = len(alphabep)

#Вычисляем минимальную длинну пароля L
L = math.ceil(S_star ** (1/A))

#Вывод минимальной длины пароля
print("(L):", L)

def generate_password(length, charset):
    return ''.join(random.choice(charset) for _ in range(length))

#Генерация случайного пароля с длинной L и использованием алфавита
password = generate_password(L, alphabep)

#Вывод
print(":", password)
print(":", L)
print(A)