def announce(f):
    def wrapper():
        print("beginning to run code")
        f()
        print("well done!")
    return wrapper


@announce
def hello():
    print("hello,world!")

# @announce
hello()

#原理明白了，但代码的每一步运行不是很清晰。