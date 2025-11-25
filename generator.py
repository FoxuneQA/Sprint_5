import random
import string

def generate_unique_email():
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"geo_test_{random_part}@yandex.ru"

def generate_password(length=8):
    if length < 6:
        length = 6
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))