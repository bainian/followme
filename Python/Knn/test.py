from __builtin__ import reduce
from numpy import *

n = ones((2, 4))
print(n)
print(ones((2, 1)))
l = [1, 2, 3, 4]
print(n * l)
print(sum(n * l))
print(random.uniform(0, 20))

str = '''
PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
892,3,"Kelly, Mr. James",male,34.5,0,0,330911,7.8292,,Q
893,3,"Wilkes, Mrs. James (Ellen Needs)",female,47,1,0,363272,7,,S
894,2,"Myles, Mr. Thomas Francis",male,62,0,0,240276,9.6875,,Q
895,3,"Wirz, Mr. Albert",male,27,0,0,315154,8.6625,,S
'''
lines = str.split("\n")
data = []
for line in lines:
    data.append(line.strip().split(',')[0])

# arr = mat(data)
# arr = arr.transpose()
# print(arr)
# for i in range(arr.shape[0]):
#     if (i > 2):
#         print(arr[i])
#     continue
#     print('---')

for i in range(2, 9):
    if i == 3: print('i == 3'); continue
    print(i)

