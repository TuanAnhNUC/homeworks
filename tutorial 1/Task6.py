print("Enter the numbers to compare (Enter consecutively without spaces, commas or periods)")
value = input('Numbers: ')
length = len(value)
i = 0
a = int(value[0])
while i < length:
    if int(value[i]) < a:
        a = int(value[i])
    i += 1
print('The smallest number is: ', a)


