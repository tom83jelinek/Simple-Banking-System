def is_prime(integer):
    integers = []
    primes = []

    for num in range(2, integer + 1):
        integers.append(num)

    while integers:
        prime = integers.pop(0)
        primes.append(prime)

        for num in integers:
            if num % prime == 0:
                integers.remove(num)

    return primes


number = int(input())

if number in (is_prime(number)):
    print('This number is prime')
else:
    print('This number is not prime')
