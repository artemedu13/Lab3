import random

def get_unique_list_numbers(a, b) -> list[int]:
    unique_numbers = []
    while len(unique_numbers) < 15:
        number = random.randint(a, b)
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers

list_unique_numbers = get_unique_list_numbers(-10, 10)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
#Ответ
