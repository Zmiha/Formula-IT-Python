numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
length = len(numbers)
f = 0
for i in range(length):
    if numbers[i] is None:
        f = i
        numbers[i] = 0
sum_ = sum(numbers)
numbers[f] = sum_/length
print("Измененный список:", numbers)
