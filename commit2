import string
import random

length = int(input("Введите длину пароля: "))
Quantity = int(input("Введите нужное кол-во паролей: "))

char_set = string.ascii_letters + string.digits

def generate_password(length, char_set):
    password = ""
    for _ in range(length):
        password += random.choice(char_set)
    return password

def generate_multiple_passwords(quantity, length, char_set):
    passwords = []
    for _ in range(quantity):
        passwords.append(generate_password(length, char_set))
    return passwords

passwords = generate_multiple_passwords(Quantity, length, char_set)
for i, pwd in enumerate(passwords, start=1):
    print(f"Пароль {i}: {pwd}")
