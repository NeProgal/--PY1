list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_i = 0
max_num = list_numbers[max_i]

for i, actual in enumerate(list_numbers):
    if actual > max_num:
        max_i = i
        max_num = actual

list_numbers[max_i], list_numbers[-1] = list_numbers[-1], list_numbers[max_i]


print(list_numbers)
