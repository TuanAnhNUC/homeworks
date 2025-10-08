import time
while True:
    n = int(input('N =  '))
    if n <= 0:
        print('Please enter a number greater than 0')
        continue
    else:
        break

i = 1
a = 0
while i <= n:
    a = a + 1/i
    i += 1
print('Sum = ', a)
time.sleep(3)