def below_arithmetical_mean(data: list):
    mean = sum(data) / len(data)
    result = []
    for number in data:
        if number < mean:
            result.append(number)
    print(result)
    return result


def two_lowest_elements(data: list):
    first_min: int = data[0]
    second_min: int = data[1]
    for number in data:
        if number < first_min and number != second_min:
            first_min = number
            continue
        if number != first_min and number < second_min:
            second_min = number
    print(first_min, second_min)


below_arithmetical_mean([1, 3, 5, 6, 4, 10, 2, 3])
two_lowest_elements([198, 3, 4, 9, 10, 9, 2])