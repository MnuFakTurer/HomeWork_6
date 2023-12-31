import random

# task 1

# def multiply_list(lead_in):
#     result = 1
#     for num in lead_in:
#         result *= num
#     return result
#
#
# random_list = []
#
# for i in range(10):
#     random_list.append(random.randint(1, 11))
#
# print(f"Random List: {random_list}")
# print(f"Product of elements in a list: {multiply_list(random_list)}")

# task 2

# def find_min(list):
#     mearning = list[0] if list else None
#     for num in list:
#         if num < mearning:
#             mearning = num
#     return mearning
#
#
#
# random_list = []
#
# for i in range(10):
#     random_list.append(random.randint(1, 500))
#
# print(f"Random List: {random_list}")
# print(f"Product of elements in a list: {find_min(random_list)}")

# task 3

# def quantity_prime_number(num_list):
#     def prime_number(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     count = 0
#     for num in num_list:
#         if prime_number(num):
#             count += 1
#     return count
#
# random_list = []
#
# for i in range(10):
#     random_list.append(random.randint(1, 100))
#
# num_primes = quantity_prime_number(random_list)
#
# print(f"Random List: {random_list}")
# print(f"Product of elements in a list: {num_primes}")

# task 4

# def remove_number(number, number_remove):
#     new_list = []
#     count = 0
#
#     for element in number:
#         if element != number_remove:
#             new_list.append(element)
#         else:
#             count += 1
#
#     return count, new_list
#
#
# random_list = []
#
# for i in range(10):
#     random_list.append(random.randint(1, 11))
#
# number_remove = random.choice(random_list)
# count, new_list = remove_number(random_list, number_remove)
#
#
#
# print(f"Random List: {random_list}")
# print(f"Number to remove: {number_remove}")
# print(f"Number og items removed: {count}")
# print(f"Modified list: {new_list}")

# task 5

# def united_list(list_one, list_two):
#     united = list_one + list_two
#     return united
#
# random_list_one = []
# random_list_two = []
#
# for i in range(10):
#     random_number = random.randint(1, 50)
#     if random_number % 2 == 0:
#         random_list_one.append(random_number)
#     else:
#         random_list_two.append(random_number)
#
# united = united_list(random_list_one, random_list_two)
# print(f"Random list one: {random_list_one}"
#       f"\nRandom list two: {random_list_two}")
# print(f"Connected list: {united}")

# task 6

def degree_number(list_number, degree_list):
    result = []
    for i in list_number:
        result.append(i ** degree_list)

    return result

try:

    random_list = []

    for i in range(10):
        random_list.append(random.randint(1, 11))

    user_degree = int(input("Enter degree: "))
    result = degree_number(random_list, user_degree)

    print(f"Random list: {random_list}")
    print(f"List the degree: {result}")

except Exception as error:
    print(error)
