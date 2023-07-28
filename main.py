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

