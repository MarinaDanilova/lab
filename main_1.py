numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers[4] = 0
total = sum(numbers)
count = len(numbers)
mean = total / count
numbers[4] = mean
print("Измененный список:", numbers)
