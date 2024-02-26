import time


def run(func, rounds, args=None):
    average_time = 0
    for i in range(rounds):
        start_time = time.time()
        func(args)
        end_time = time.time()
        average_time = (average_time * i + end_time - start_time) / (i + 1)
    print(f"{func.__name__}: {average_time=}s")
    return average_time


def compare_array_append_1(args=None):
    a = []
    for i in range(10000):
        a += [i]


def compare_array_append_2(args=None):
    a = []
    for i in range(10000):
        a.append(i)


def compare_enumerate_1(l):
	for i, el in enumerate(l):
		thing = el + i


def compare_enumerate_2(l):
	i = 0
	for el in l:
		thing = el + i
		i += 1


def compare_enumerate_3(l):
	n = len(l)
	i = 0
	while i <= n - 1:
		thing = l[i] + i
		i += 1


def compare_enumerate_4(l):
	n = len(l)
	for i in range(n):
		thing = l[i] + i


def compare_for_loop_1(l):
	n = len(l)
	for i in range(n):
		thing = l[i] * 2


def compare_for_loop_2(l):
	for el in l:
		thing = el * 2


a = run(func=compare_array_append_1, rounds=1000)  # a += [i]
b = run(func=compare_array_append_2, rounds=1000)  # a.append(i)
times_faster = round(a/b, 1)
print(f"\n'a.append(i)' is {times_faster}x faster than 'a += [i]'. usually 1.6x ~ 2.0x faster\n")
# result: 1.6x ~ 2.0x faster

arr = [i for i in range(10000)]
c = run(func=compare_enumerate_1, rounds=1000, args=arr)  # for i, el in enumerate(l)
d = run(func=compare_enumerate_2, rounds=1000, args=arr)  # for el in l
e = run(func=compare_enumerate_3, rounds=1000, args=arr)  # while i <= n - 1
f = run(func=compare_enumerate_4, rounds=1000, args=arr)  # for i in range(n)
times_faster = round(d/c, 1)
print(f"\n'for i, el in enumerate(l)' is {times_faster}x faster than 'for el in l'; almost the same. usually 1:1 plus or minus 0.1")
times_faster = round(((c + d) / 2) / f, 1)
print(f"'for i in range(n)' is fastest, just slightly, at {times_faster}x faster than the previous two. usually 1.1x ~ 1.3x faster")
times_faster = round(e/f, 1)
print(f"and 'while i <= n - 1' is the slowest, where 'for i in range(n)' is {times_faster}x faster than it. usually 1.5x ~ 2.0x faster\n")

g = run(func=compare_for_loop_1, rounds=1000, args=arr)  # for i in range(n)
h = run(func=compare_for_loop_2, rounds=1000, args=arr)  # for el in l
times_faster = round(g/h, 1)
print(f"\n'for el in l' is {times_faster}x faster than 'for i in range(n)' comparing just looping elements; usually 1.3x ~ 1.5x faster\n")
