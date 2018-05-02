import sched, time


# This program prints Hello, world!

print('Hello, world!')



s = sched.scheduler(time.time, time.sleep)
def print_time(a='default'):
    print('From print_time', time.time(), a)
def print_some_times():
    print(time.time())
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('positional',))
    s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
    s.enter(2, 1, print_time)
    s.run()
    print(time.time())


print_some_times()
