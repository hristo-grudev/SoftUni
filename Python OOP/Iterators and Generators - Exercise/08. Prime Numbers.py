def is_prime(num):
    # if num < 2:
    #     return False
    # for i in range(2, num):
    #     if num % i == 0:
    #         return False
    # return True
    return num > 1 and all(num % i for i in range(2, num))

def get_primes(seq):
    primes = filter(lambda n: is_prime(n), seq)
    for num in primes:
        yield num