#一个类由属性和method（method必须依附于变量使用）
# 还有一个问题：这个代码是如何迭代的？将乘客座位累加至3？
class Flight():
    def __init__(self,capacity):  #初始化类的属性------飞机的容量(或者剩余的容量)以及乘客座位的顺序是属性
        self.capacity = capacity #self指的是变量本身哦
        self.passagers = []

    #定义内部函数（即method）,实现功能------能载客多少人是功能
    def add_passager(self,name):
        # if not self.capacity():
        if not self.open_seats():
            return False
        self.passagers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passagers)



flight = Flight(3)#这里以后写代码的时候提醒人们只能input数字。

people = ["harry","mary","mardin","chen shude","chen zhihui"]
for person in people : #从这里就能看出来，for-loop具有迭代性，passagers-list内的名字循环一次增加一次。
    #sucess = Flight.add_passager(person)

    if flight.add_passager(person) : # person equals name here,判断success的值是true 或者false
        print(f"{person} successfully is added")
    else :
        print(f"No available seats now for {person}")
