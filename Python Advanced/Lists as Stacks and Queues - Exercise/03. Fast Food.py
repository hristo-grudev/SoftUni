from collections import deque

total_qty = int(input())

orders_queue = deque(map(int, input().split(' ')))

print(max(orders_queue))

while orders_queue:
	order = orders_queue.popleft()

	if total_qty >= order:
		total_qty -= order
	else:
		orders_queue.appendleft(order)
		break

if orders_queue:
	orders_left = ' '.join(list(map(str, orders_queue)))
	print(f'Orders left: {orders_left}')
else:
	print('Orders complete')
