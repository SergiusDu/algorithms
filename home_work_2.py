def evens_first(data: list):
    for index in range(len(data)):
        element = data[index]
        if not (element % 2):
            data.insert(0, data.pop(index))
    print(data)
    return data


def increment_number(data: list):
    result = []
    for number in data:
        result.append((number + 1) % 10)
    print(result)
    return result


evens_first([7, 3, 5, 6, 4, 10, 3, 2])
increment_number([1, 2, 9] )