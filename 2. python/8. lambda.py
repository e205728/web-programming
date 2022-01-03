people = [
    {"name" : "chen","house" : "beijing"},
    {"name" : "wang","house" : "shanghai"},
    {"name" : "zhao","house" : "guangdong"}
]



####第一种方法排序####
# def f(person):
#     # return person("name")
#     return person["house"]#为什么是中括号

# people.sort(key=f)
# print(people)

# print(len(people))



####第二种方法排序####
people.sort(key=lambda person:person["house"])#为什么是中括号
print(people)

print(len(people))