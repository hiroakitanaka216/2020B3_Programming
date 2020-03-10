str = "Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
list = str.split(" ")
print(list)
dic = {}

one = [0, 4, 5, 6, 7, 8, 14, 15, 18]

for i in range(0, len(list)):
    s = list[i]
    if i in one:
        dic[s[0]] = i + 1
    else:
        dic[s[0:2]] = i + 1
print(dic)
