# bai 1
a = int(input('a='))
b = int(input('b='))
print(a, b)
a,b = b,a

print(a, b)


# bai 2
the_number = [0, 34, 21, 6, 7, 12, 7, 92]
x=7
list1 = []
list2 = the_number.copy()

for i in the_number:
    list1.append(i)
    list2.remove(i)
    if i==x:
        break
print('list1', list1)
print('list1', list2)
