import heapdict
h=heapdict.heapdict()

h[2]=3
h[4]=1
h[5]=2
h[3]=4

#print(h.peekitem()) #return high priority value
#print(h.popitem()) #remove and return high priority value

print(h.get(3))

while len(h):
    x=h.popitem()
    print(x)
