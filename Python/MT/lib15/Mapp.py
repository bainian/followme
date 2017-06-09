import sys
from numpy import mat, mean, power


def read_line(file):
    for line in file:
        yield line.rstrip()


input = read_line(sys.stdin) # generator input, used for invoke
print(type(input))
input = [float(line) for line in input]
print((type(input)))
print(input)
numInput = len(input)
input = mat(input)
print(type(input))
print(input)
sqInput = power(input, 2)
print(type(sqInput))
print(sqInput)
print('%d\t%f\t%f\t ' % (numInput, mean(input), mean(sqInput)))
