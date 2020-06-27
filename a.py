def decorator(func):
    def b():
        print("world")
        return func()
    return(b)


def a():
    print("hello")
ab = decorator(a)
ab()