def custom_map(function):
    def wrapper(sequence):
        # Apply function to all the elements of sequence
        return [function(item) for item in sequence]

    return wrapper


def square(number):
    return number * number


@custom_map
def mapper(function, list):
    pass 