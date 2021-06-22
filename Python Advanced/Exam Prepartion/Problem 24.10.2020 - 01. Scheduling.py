from heapq import heappush, heappop


def read_input():
	return map(int, input().split(', ')), int(input())


def min_cycles_for_job(jobs, job_index):
	sorted_jobs = sorted(
		[(v, i) for (i, v) in enumerate(jobs)]
	)
	cycles = 0
	for (job, index) in sorted_jobs:
		cycles += job
		if index == job_index:
			break
	return cycles


def min_cycles_for_job_heap(jobs, job_index):
	heap = []
	for index, job in enumerate(jobs):
		heappush(heap, (job, index))

	cycles = 0
	while True:
		job, index = heappop(heap)
		cycles += job
		if index == job_index:
			break


def print_result(result):
	print(result)


jobs, job_index = read_input()
result = min_cycles_for_job(jobs, job_index)
print_result(result)
