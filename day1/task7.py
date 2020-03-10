string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
string = string.replace(",", "")
string = string.replace(".", "")
my_list = string.split(" ")
print(my_list)
l = [len(word) for word in my_list]
print(l)
