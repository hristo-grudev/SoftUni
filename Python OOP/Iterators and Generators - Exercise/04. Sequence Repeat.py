class sequence_repeat:
    def __init__(self, seq, count):
        self.seq = seq
        self.count = count
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= self.count:
            raise StopIteration
        idx = self.current_index
        self.current_index += 1
        return self.seq[idx % len(self.seq)]

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
