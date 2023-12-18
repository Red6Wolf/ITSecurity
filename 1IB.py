import random

user_indentifier = input("Введите индетификатор пользователя: ")

password_length = 12

N = len(user_indentifier)
Q = N**3 % 5
P = N**2 % 6

lowercase_russian_alhabet = "абвгдеёжзийклмнопрстуфхцчщзъыьэюя"
uppercase_russia_alhabet = lowercase_russian_alhabet.upper()

password = ""

for i in range(Q):
    password += random.choice(lowercase_russian_alhabet)
    

for i in range (P):
    password += random.choice(uppercase_russia_alhabet)
    
    
remining_chars = password_length - Q - P
for i in range(remining_chars):
    password += str(random.randint(0, 9))
    
    
password = ''.join(random.sample(password, len(password)))

print("Сгенерированный пароль:", password)