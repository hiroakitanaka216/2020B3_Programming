import sys
import random

args = sys.argv

for i in range(1,len(args)+1):
    s = args[i]
    t = s[1:len(s)-1]
    s0 = s[0]
    sl = s[len(s)-1]
    tr = ''.join(random.sample(t, len(t)))
    u = s0 + tr + sl
    print(u)

