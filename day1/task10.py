import sys

args = sys.argv

words_list = []
char_list = []

for i in range(1, len(args)-1):
    s = args[i]+','+args[i+1]
    words_list.append(s)
print(words_list)

t = args[1]
for j in range(1, len(args)-1):
    t = t+args[j+1]

for k in range(0, len(t)-1):
    u = t[k]+t[k+1]
    char_list.append(u)
print(char_list)
