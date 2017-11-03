a = 1
b = 2
c = 0
total = 0

while c <=4000000:
    c = b
    if b % 2 == 0:
        total += b
    c = a + b
    a = b
    b = c

print total