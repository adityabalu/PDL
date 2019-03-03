

def gen():
    n = 0
    while True:
        n += 1
        yield n


if __name__ == '__main__':
    a = gen()
    print(a)
    for _ in range(10):
        print(next(a))