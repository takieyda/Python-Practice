a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

#main
for item in a:
    if item < 5:
        print item

#extra 2
for item in a:
    if item < 5:
        b.append(item)
print(b)
        
#extra 3
num = raw_input("Number? ")

c = []

for item in a:
    if item < int(num):
        c.append(item)
print(c)

#adreaofhodor comment
list2 = [i for i in a if i < 5]
print(list2)
