# STRETCH GOAL 3

# Write a program to determine if a number, given on the command line, is prime.

x = input("Enter a number: ")


def is_prime(number):
    num = int(number)
    if num > 1:
        for i in range(2, num):
            if(num % 2 == 0):
                print(f'The number {num} is NOT prime')
                break
        else:
            print(f'The number {num} IS prime')

    else:
        print(f'The number {num} is NOT prime')


is_prime(x)

# How can you optimize this program?
# Implement The Sieve of Eratosthenes, one of the oldest algorithms known (ca. 200 BC)
