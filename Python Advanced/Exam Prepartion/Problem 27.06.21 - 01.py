from collections import deque

chocolates = [int(el) for el in input().split(', ')]
cups_of_milks = [int(el) for el in input().split(', ')]


# chocolates = [-10, -2, -30, 10]
# cups_of_milks = [-5]

cups_of_milks = deque(cups_of_milks)

milkshake = 0

while True:
    if len(chocolates) == 0 or len(cups_of_milks) == 0:
        break
    if chocolates[-1] <= 0:
        chocolates.pop()
    if cups_of_milks[0] <= 0:
        cups_of_milks.popleft()

    if len(chocolates) == 0 or len(cups_of_milks) == 0:
        break

    if chocolates[-1] > 0 and cups_of_milks[0] > 0:
        if chocolates[-1] == cups_of_milks[0]:
            milkshake += 1
            chocolates.pop()
            cups_of_milks.popleft()
            if milkshake == 5:
                break

        else:
            cups_of_milks.rotate(-1)
            chocolates[-1] -= 5


if milkshake == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if len(chocolates) == 0:
    print(f'Chocolate: empty')
else:
    print(f'Chocolate: {", ".join([str(el) for el in chocolates])}')
if len(cups_of_milks) == 0:
    print(f'Milk: empty')
else:
    print(f'Milk: {", ".join([str(el) for el in cups_of_milks])}')
