import wikipedia

query = "Austria"
query_bak = query
query = wikipedia.summary(query)
query = '.'.join(query.split('.')[:3]) + '.'

"""ret = ''
skip1c = 0
skip2c = 0
for i in query:
    if i == '(':
        skip1c += 1
    elif i == ')'and skip2c > 0:
        skip2c -= 1
    elif skip1c == 0 and skip2c == 0:
        ret += i"""

ret = ''
skip1c = 0
skip2c = 0
for i in query:
    if i == '[':
        skip1c += 1
    elif i == '(':
        skip2c += 1
    elif i == ']' and skip1c > 0:
        skip1c -= 1
    elif i == ')'and skip2c > 0:
        skip2c -= 1
    elif skip1c == 0 and skip2c == 0:
        ret += i
print(ret)



