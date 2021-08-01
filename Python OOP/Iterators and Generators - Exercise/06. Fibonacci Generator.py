def fibonacci():
    f_1 = 0
    f_2 = 1
    yield f_1
    yield f_2

    fn_1 = f_2
    fn_2 = f_1
    while True:
        fn = fn_2 + fn_1
        yield fn
        fn_2 = fn_1
        fn_1 = fn
