import sys

args = sys.argv

words_list = []
char_list = []

num = 2

for i in range(1, len(args) - num + 1):
    s = args[i:i+num]
    words_list.append(s)
print(words_list)

t = "****".join(args[1:])
print(t)

for k in range(0, len(t)-1):
    u = t[k:k+num]
    char_list.append(u)
print(char_list)
