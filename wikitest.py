import wikipedia
x = "Modi"
x = wikipedia.summary(x)

x = '.'.join(x.split('.')[:3]) + '.'
x = 'hey (this is (sharan and his (useless) friend) asus tuf).'

"""for line in x.split('.'):
    c = 0
    while True:
        s = line.find('(')
        if s is -1: break
        c = 1
        i = 0
        for ch in line:
            i += 1
            if c is 0:
                break
            if ch is '(':
                c += 1
            elif ch is ')':
                c -= 1
        line = line[:s-1] + line[i+1:]
    print(line)"""


ret = ''
skip1c = 0
skip2c = 0
for i in x:
    if i == '(':
        skip1c += 1
    elif i == ')'and skip2c > 0:
        skip2c -= 1
    elif skip1c == 0 and skip2c == 0:
        ret += i

print(ret)

