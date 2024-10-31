# Task 1  
# number = int(input("Enter number: "))

# if number > 0:
#     print(number + 1)
# else:
#     print(number)


# Task 2
# number = int(input("Enter number: "))

# if number > 0: 
#     number += 1
# elif number < 0: 
#     number -= 2
# else: 
#     print("Error")

# print(number)


# Task 3
# number = int(input("Enter number: "))
# if number != 0: 
#     if number > 0:
#         number += 1
#     elif number < 0:
#         number -= 2
# else:
#     number += 10

# print(number)



# Task 4-5 
# first_num = int(input("First number: "))
# second_num = int(input("Second number: "))
# third_num = int(input("Enter number: "))
# print("\n\n\n")
# positive = 0
# negative = 0
# if first_num > 0: 
#     positive += 1
#     print(f"{first_num} - positive")
# elif first_num < 0:
#     negative += 1
#     print(f"{first_num} - negative")

# if second_num > 0:
#     positive += 1
#     print(f"{second_num} - positive")
# elif second_num < 0:
#     negative += 1
#     print(f"{second_num} - negative")

# if third_num > 0:
#     positive += 1
#     print(f"{third_num} - positive")
# elif third_num < 0:
#     negative += 1
#     print(f"{third_num} - negative")

# print("\n\n\n")

# print(f"positive numbers: {positive} \nnegative: {negative}")
# print("\n\n\n")


# Task 6
# a = int(input("a: "))
# b = int(input("b: "))

# if a > b:
#     print("a katta")
# elif b < a:
#     print("b katta")
    

# Task 7 
# a = int(input("a: "))
# b = int(input("b: "))

# if a > b:
#     print(f"\n\nb: kichik\ntartib raqami: 2")
# elif a < b:
#     print(f"\n\na: kichik\ntartib raqami: 1")
# elif a == b:
#     print("ikkalovsi teng")

# list_number = []
# list_number.append(a)
# list_number.append(b)
# print(list_number)



# Task 8 
# a = int(input("a: "))
# b = int(input("b: "))

# index = 0

# if a > b: 
#     index = 1

# if index == 1: 
#     print(f"{a}, {b}")
# elif index == 0:
#     print(f"{b}, {a}")



# # Task 9 
# a = int(input("a: "))
# b = int(input("b: "))

# if a > b:
#     a -= a

# print(f"a: {a} , b: {b}")



# Task 10 
# a = int(input("a: "))
# b = int(input("b: "))

# if a != b:
#     sum_ab = a + b
#     a = sum_ab
#     b = sum_ab
#     #alternative
#     #a = b = a + b
#     print(f"a = {a}, b = {b}")
# elif a == b:
#     print(f"a = {a}, b = {b}")


# Task 11 
# a = int(input("a: "))
# b = int(input("b: "))

# mind = int()

# if a != b:
#     if a < b:
#         mind = b
#     elif a > b:
#         mind = a
#     print(f"a = {mind}, b = {mind}")
# elif a == b:
#     print(f"a = {a}, b = {b}")

# alternative 
# if a != b:
#     max_val = max(a, b)
#     a = b = max_val
#     print(f"a = {a}, b = {    b}")
# else:
#     print(f"a = {a}, b = {b}")


# Task 12 
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# min_val = min(a, b, c)

# print(min_val)

# Task 13
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# max_val = max(a,b,c)
# min_val = min(a,b,c)

# if a != max_val and a != min_val:   
#     mid_val = a
# elif b != max_val and b != min_val:
#     mid_val = b
# else: 
#     mid_val = c

# print(f"midle value: {mid_val}")



# Task 14 
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))


# print(f"kichik son: {min(a,c,b)} kattason son: {max(a,b,c)}")


# Task 15
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# sum_ab = a + b
# sum_ac = a + c
# sum_bc = b + c

# if sum_ab >= sum_ac and sum_ab >= sum_bc:
#     print(a, b)
# elif sum_ac >= sum_ab and sum_ac >= sum_bc:
#     print(a, c)
# else:
#     print(b, c)



# Task 16 
# A = float(input("Введите число A: "))
# B = float(input("Введите число B: "))
# C = float(input("Введите число C: "))

# if A < B < C:
#     A, B, C = A * 2, B * 2, C * 2
# else:
#     A, B, C = -A, -B, -C

# print(f"A = {A}, B = {B}, C = {C}")



# Task 17 
# A = float(input("Введите число A: "))
# B = float(input("Введите число B: "))
# C = float(input("Введите число C: "))

# if A < B < C or A > B > C:
#     A, B, C = A * 2, B * 2, C * 2
# else:
#     A, B, C = -A, -B, -C

# print(f"A = {A}, B = {B}, C = {C}")


# Task 18 
# A = int(input("Введите число A: "))
# B = int(input("Введите число B: "))
# C = int(input("Введите число C: "))

# if A == B:
#     index = 3  # Индекс числа C
# elif A == C:
#     index = 2  # Индекс числа B
# else:
#     index = 1  # Индекс числа A

# print(f"Индекс отличающегося числа: {index}")


# Task 19 
# A = int(input("Введите число A: "))
# B = int(input("Введите число B: "))
# C = int(input("Введите число C: "))
# D = int(input("Введите число D: "))

# if A == B == C:
#     index = 4  # Индекс числа D
# elif A == B == D:
#     index = 3  # Индекс числа C
# elif A == C == D:
#     index = 2  # Индекс числа B
# else:
#     index = 1  # Индекс числа A

# print(f"Индекс отличающегося числа: {index}")


# Task 20 
# A = float(input("Введите координату точки A: "))
# B = float(input("Введите координату точки B: "))
# C = float(input("Введите координату точки C: "))

# dist_B = abs(B - A)
# dist_C = abs(C - A)

# if dist_B < dist_C:
#     closest_point = B
#     distance = dist_B
# else:
#     closest_point = C
#     distance = dist_C

# print(f"Ближайшая точка: {closest_point}, Расстояние: {distance}")



# Task 21 
# x = int(input("Введите координату x: "))
# y = int(input("Введите координату y: "))

# if x == 0 and y == 0:
#     result = 0
# elif x == 0:
#     result = 2
# elif y == 0:
#     result = 1
# else:
#     result = 3

# print(result)



# Task 22 
# x = int(input("Введите координату x: "))
# y = int(input("Введите координату y: "))

# if x > 0 and y > 0:
#     quadrant = 1
# elif x < 0 and y > 0:
#     quadrant = 2
# elif x < 0 and y < 0:
#     quadrant = 3
# else:
#     quadrant = 4

# print(f"Четверть: {quadrant}")



# Task 23 
# x1 = int(input("Введите координату x1: "))
# y1 = int(input("Введите координату y1: "))
# x2 = int(input("Введите координату x2: "))
# y2 = int(input("Введите координату y2: "))
# x3 = int(input("Введите координату x3: "))
# y3 = int(input("Введите координату y3: "))

# # Ищем четвертую координату по уникальным значениям осей
# x4 = x1 ^ x2 ^ x3
# y4 = y1 ^ y2 ^ y3

# print(f"Координаты четвертой вершины: ({x4}, {y4})")


