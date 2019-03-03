


def func1(fn):
    def inner():
        fn()
        print('text 1')
    return inner

@func1
def func2():
    print('text 2')


if __name__ == '__main__':
    func2()