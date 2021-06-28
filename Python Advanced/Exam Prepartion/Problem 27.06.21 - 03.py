def math_operations(*args, **kwargs):
    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return x
        return x / y

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    help_dict = {0: 'a', 1: "s", 2: "d", 3: 'm'}
    sign_dict = {0: add, 1: subtract, 2: divide, 3: multiply}
    numbers = args
    final_dict = kwargs
    counter = 0
    for number in numbers:
        final_dict[help_dict[counter]] = sign_dict[counter](final_dict[help_dict[counter]], number)
        counter += 1
        if counter == 4:
            counter = 0

    return final_dict
