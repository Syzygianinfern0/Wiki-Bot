import wikipedia
x = "Modi"
x = wikipedia.summary(x)

x = '.'.join(x.split('.')[:3]) + '.'
x = 'hey (this is (sharan and his (useless) friend) asus tuf)'
while True:
    s = x.find('(')
    """ if s is -1:
        break
    e = x.find(')')
    if s > e:
        x = x[:e] + x[e+1:]
        continue
    x = x[:s-1] + x[e+1:]"""
    e = x.find(')')
    if s is -1 and e is -1:
        break
    if s > e:
        x = x[:e] + x[e+1:]
        continue
    if s is -1:
        x = x[:e] + x[e+1:]
        continue
    x = x[:s-1] + x[e+1:]
print(x)
