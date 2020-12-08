a = int(input())
b = int(input())

firstA = a
firstB = b

a = firstB
b = firstA

print('Before:')
print(f'a = {firstA}')
print(f'b = {firstB}')
print('After:')
print(f'a = {a}')
print(f'b = {b}')