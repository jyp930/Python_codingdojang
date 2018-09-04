from itertools import *

def cmpr(li):
    c = combinations((x for x in range(len(li))), len(li)//2)
    m = []
    for x in c:
        a = []
        b = []
        s = set(x)
        ran = set(x for x in range(len(li)))
        s = ran - s
        for y in x:
            a.append(li[y])
        for z in s:
            b.append(li[z])
        if m == []:
            m.append(a)
            m.append(b)
        if abs(sum(a)-sum(b)) < abs(sum(m[0])-sum(m[1])):
            m[0] = a
            m[1] = b

    return sum(m[0]), sum(m[1])

while __name__ == '__main__':
    num = int(input('사람 수: '))
    pe = []
    for i in range(num):pe.append(int(input('{0}명째: '.format(i+1))))
    print(cmpr(pe))
