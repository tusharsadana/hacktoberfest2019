data = b'abc'

def m1(x):
    return x.split(b'\n', 1)[1]

def m2(x):
    return x[x.index(b'\n')+1:]


if __name__ == '__main__':
    import timeit

    print(r"x.split(b'\n', 1)[1] : ", timeit.timeit(stmt="m1(data)",
                        setup="from __main__ import m1, data",
                        number=100000))
    print(r"x[x.index(b'\n')+1:] : ", timeit.timeit(stmt="m2(data)",
                        setup="from __main__ import m2, data",
                        number=100000))
