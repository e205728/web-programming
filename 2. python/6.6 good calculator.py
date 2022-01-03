
class Calculator:#对于类的定义我们要求首字母大写
    name ='Good calculator'#固有属性项
    price =20
 
    def __init__(self,name,price,H,width=10,weight=5):#初始化类的属性
        self.name=name
        self.p=price
        self.h=H
        self.wi=width
        self.we=weight
 
    #定义内部函数,实现功能
    def add(self,x,y):#self 表示本类
        print(self.name)#在类中使用self调用它的名字
        result = x+y
        print(result)
 
    def minus(self,x,y):
        result = x-y
        print(result)
 
    def times(self,x,y):
        result = x*y
        print(result)
 
    def divide(self,x,y):
        result = x/y



c = Calculator('CC',20,30)#定义实例来使用该类
#打印出实例中任何你想要的属性值
#使用格式：class.name.属性
 
print(c.name)#默认名称
print(c.n)#实例中名称
print(c.price)#默认的价格属性
print(c.p)#实例中赋予的价格属性
print(c.h)#实例中高度值
print(c.we)#实例中宽度