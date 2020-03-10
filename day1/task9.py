import sys
import random

args = sys.argv

for word in args[1:]:
    if len(word) >= 4:
        t = word[1:-1]
        tr = ''.join(random.sample(t, len(t)))
        u = word[0] + tr + word[-1]

    else:
        u = word

    print(u, end=" ")
print()