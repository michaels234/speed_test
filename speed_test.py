import time


def run(func, rounds):
    average_time = 0
    for i in range(rounds):
        start_time = time.time()
        func()
        end_time = time.time()
        average_time = (average_time * i + end_time - start_time) / (i + 1)
    print(f"{func.__name__}: {average_time=}s")
    return average_time


def array_plus_equals():
    a = []
    for i in range(10000):
        a += [i]


def array_append():
    a = []
    for i in range(10000):
        a.append(i)


a = run(func=array_plus_equals, rounds=1000)
b = run(func=array_append, rounds=1000)
times_faster = round(a/b, 1)
print(f"array_append is {times_faster}x faster than array_plus_equals")
# result: 1.8x faster
