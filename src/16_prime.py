# STRETCH GOAL 3

# Write a program to determine if a number, given on the command line, is prime.

import math

x = input("Enter a number: ")


def is_prime(number):
    num = int(number)
    if num > 1:
        for i in range(2, num):
            if(num % i == 0):
                print(f'The number {num} is NOT prime')
                return False
                break
        else:
            print(f'The number {num} IS prime')
            return True

    else:
        print(f'The number {num} is NOT prime')
        return False


is_prime(x)

# IMPROVEMENTS in line 11

# Victor's example

# def is_prime_1(num):
#     sqrt = math.floor(math.sqrt(num))
#     if (num <= 1):
#         return num >= 1
#     for i in range(2, sqrt + 1):
#         if num % i == 0:
#             return False
#     return True


# Implement The Sieve of Eratosthenes, one of the oldest algorithms known (ca. 200 BC)

y = input("Get a list of prime numbers up to: ")


def eratosthenes(number):
    limit = int(number) + 1
    prime_lst = []
    not_prime = []

    for num in range(limit):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    not_prime.append(num)
            else:
                prime_lst.append(num)

        else:
            not_prime.append(num)

    print(prime_lst)


eratosthenes(y)

# Victor's example

# def daSieve(n):
#     p = 2
#     prime = [True for i in range(n + 1)]
#     for i in range(p, math.floor(math.sqrt(n))):
#         if prime[i]:
#             for j in range(i**2, n + 1, i):
#                 prime[j] = False
#     for i in range(n + 1):
#         if prime[i]:
#             print(i, end=(", "))
