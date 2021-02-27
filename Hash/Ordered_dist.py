from collections import OrderedDict
od=OrderedDict()
ar=[1,1,1,3,2,2,2,3]
for i in ar:
    od[i]=od.get(i,0)+1
#od.move_to_end(1)
print(od)
x=od.pop(1)
#print(x)
od[1]=x
print(od)
