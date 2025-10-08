# nhap a=4
# nhap b=8
a = 4
b = 8
# Thuat toan
if a<b:
    a = a + 2 * b
    if a<20:
        b += 10
    else:
        b = b + 5 * a
else:
    a = a**2 + b
    b = b + 5 * a

print("a=", a, "b=", b)
