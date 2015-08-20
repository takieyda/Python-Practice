a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#main
for item in a:          #iterate each item in list a
    if item < 5:        #if the item less than 5
        print(item)     #print the item, each on separate line

#extra 2
b = []

for item in a:          #same as before
    if item < 5:
        b.append(item)  #except appends the item to list b
print(b)                #prints list b as a whole
        
#extra 3
num = raw_input("Number? ")

c = []

for item in a:          #same as before
    if item < int(num): #checks the item against user input, as an integer
        c.append(item)  #appends to list c
print(c)

#adreaofhodor comment
list2 = [i for i in a if i < 5]
print(list2)
