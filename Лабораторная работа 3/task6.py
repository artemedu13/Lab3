list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
current_number = 0
current_index = 0

for index, num in enumerate(list_numbers):
    if num >= current_number:
        current_number = num
        current_index = index

list_numbers[current_index], list_numbers[-1] = list_numbers[-1], current_number

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
 # Ответ