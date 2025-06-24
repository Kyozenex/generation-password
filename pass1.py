import string
import random

char_set = string.ascii_letters + string.digits
def generate_password(length, char_set):
    password = ""
    for _ in range(length):
        password += random.choice(char_set)
    return password

password = generate_password(8, char_set)
print("Сгенерированный пароль:", password)
