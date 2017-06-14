wholeFile = []

f = open('t.txt')
lines = f.readlines()
for line in lines:
    print('line = ', line)
    words = line.split('\t')
    for i in words:
        wholeFile.append(i.strip())
ss = [s for s in wholeFile if s != '']
print(ss)
print(len(ss))

l = []
for j in range(len(ss)):
    if ss[j].startswith('或'):
        word = ss[j]
        ss[j - 1] = ss[j - 1] + word
        l.append(j)
for i in l:
    ss.pop(i)
f.close()
ff = open('file2.txt', 'w')
lenth = len(ss)
index = 0
for i in range(lenth):
    ff.write(ss[i])
    ff.write('\t\t')
    index += 1
    if (index % 7 == 0):
        ff.write('\n')
ff.close()
