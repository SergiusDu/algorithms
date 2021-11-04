def sum_of_digits(number):
    result = 0
    for n in range(number + 1):
        result += n
    print(result)


def find_max_number(*values):
    max_value = values[0]
    for value in values:
        max_value = max(max_value, value)
    print(max_value)


def count_odd_and_even_numbers(*numbers):
    odds = 0
    evens = 0
    for number in numbers:
        if number % 2:
            evens += 1
        else:
            odds += 1

    print(f'Odds count: {odds}\nEvens count: {evens}')


sum_of_digits(5)
find_max_number(10, 20, 30, 40, 21, 0.5)
count_odd_and_even_numbers(10, 3, 4, 2)
