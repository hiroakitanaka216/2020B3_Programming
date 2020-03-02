str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = str.strip(",")
str = str.strip(".")
list= str.split(" ")
#print(list)
l=[]
for num in range(0,15):
    l.append(len(list[num]))
print(l)
