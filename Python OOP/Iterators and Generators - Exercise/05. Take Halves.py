def solution():
    def integers():
        i = 0
        while True:
            yield i + 1
            i += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for i in range(n):
            result.append(next(seq))
        yield result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
