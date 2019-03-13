import wikipedia
x = input("Enter to search : ")
x = wikipedia.summary(x)
x = x[:300]

print(x)