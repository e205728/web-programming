

# for i in range(10):

#         print(i)
# j = []
# print(len(j))
# j.append(i)

####不可迭代####
j=[]

for name in ["harry","mary","mardin","chen shude","chen zhihui"] :
    print(name)
    # j.append(name)
j.append(name)
print(j)
print(len(j))

print("")
j=[]

####可迭代####
for name in ["harry","mary","mardin","chen shude","chen zhihui"] :
    print(name)
    print(j)
    j.append(name)

print(j)
print(len(j))


