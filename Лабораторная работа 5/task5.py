import random
symbl = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
password = symbl + digits

def get_random_password(n: int) -> str:
    return "".join(random.sample(password, n))

print(get_random_password(8))
#Ответ