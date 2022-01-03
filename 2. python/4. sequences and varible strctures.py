#### sequences####
name = "harry potter"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])

####lists####
print("")
names = ["harry_pottter","mary","queen"]
names.append("marin")
names.sort()
print(names)

####dictionaries####
vocabulary = {"a" : "a,are,am","b":"be,beach,bitch","c":"care,candy"}
vocabulary["a"] = "alarm"# 这会重置“a”中的内容只有alarm
print(vocabulary)
print(vocabulary["a"])
print(vocabulary["b"])

####set####
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(7)
s.add(6)
s.add(5)
s.add(4)
s.add(2)# a set where no elements even appars one more
s.remove(6) # remove 2 from set s.
print(s)# 由小到大，由前到后（字母）自动排序
print(f"this set has {len(s)} elements")

"""
varible strctures:
lists
tuple
set
dict
"""
