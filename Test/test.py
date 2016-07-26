import numpy;
import scipy;

def pythonsum(n):
    a = range(n)
    b = range(n)
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])

    return c



print pythonsum(6)

a = numpy.arange(6)
b = numpy.arange(6)
for i in range(len(a)):
    a[i] = i ** 2
    b[i] = i ** 3
c=a+b
print a
print b
print c


q = [[1,2,3],4,[5,6]]