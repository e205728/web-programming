
'''
如果代码中需要有一些错误，就可以用这个（try-except），或者debugging的时候。
x = int(input("x:"))
y = int(input("y:"))

results = x/y

print(f"x/y = {x/y}")
'''


'''
fackback(exceptions):
ZeroDivisionError: division by zero
so you can change code over as follows:
'''
try:
    x = int(input("x:"))
    y = int(input("y:"))

    results = x/y

    print(f"x/y = {x/y}")


except ZeroDivisionError :
    print("can not diviside by zero")

except ValueError:
    print("can not diviside by value")

