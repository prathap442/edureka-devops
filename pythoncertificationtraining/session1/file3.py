# Even numbers between 1000 and 2000
def even_numbers_getter(start_from,stop_till):
    numbers = list(range(start_from,stop_till))
    even_numbers = []
    for number in numbers:
        if((number%2) == 0):
            even_numbers.append(number)
    print(even_numbers)
    return even_numbers
even_numbers_getter(1,1000)