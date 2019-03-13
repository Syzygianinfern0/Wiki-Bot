import wikipedia
x = "egsrgr"
x = wikipedia.summary(x)
x = '.'.join(x.split('.')[:3]) + '.'
while True:
    s = x.find('(')
    if s is -1:
        break
    e = x.find(')')
    x = x[:s-1] + x[e+1:]
print(x)