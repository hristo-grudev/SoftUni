def read_next(*args):
    for current_iterable in args:
        for item in current_iterable:
            yield item
