str = "Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
list = str.split(" ")
print(list)
dic = {}
keys = []
values = []
for i in range(0, len(list)):
    if(i==0 or i==4 or i==5 or i==6 or i==7 or i==8 or i==14 or i==15 or i==18):
        s = list[i]
        keys.append(s[0])
    else:
        s = list[i]
        keys.append(s[0:2])
for j in range(0, len(list)):
    values.append(j+1)
dic = dict(zip(keys,values))
print(dic)