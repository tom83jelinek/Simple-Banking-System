def fizz_buzz(start, stop):
    for number in range(start, stop + 1):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)


first_number, last_number = 1, 100

fizz_buzz(first_number, last_number)
