def type_check(t):
    def check_accepts(func):
        def wrapper(arg):
            if type(arg) == t:
                return func(arg)
            else:
                return "Bad Type"

        return wrapper
    return check_accepts


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
