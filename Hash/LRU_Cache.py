from collections import OrderedDict
class LRU:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache=OrderedDict()
    def get(self,key):
        if key not in self.cache:
            return -1
        else:
            v=self.cache.pop(key)
            self.cache[key]=v
            #self.cache.move_to_end(key) #used recently: push to end of queue
            return self.cache[key]

    def put(self,key,value):
        self.cache[key]=value
        v=self.cache.pop(key)
        self.cache[key]=v
        #self.cache.move_to_end(key)
        if len(self.cache)>self.capacity:
            self.cache.popitem(0)  #least recently used: pop the front of queue

ob=LRU(2)
ob.put(1,1)
ob.put(2,2)
print(ob.get(1))
ob.put(3,3)
print(ob.get(2))
ob.put(4,4)
print(ob.get(3))
print(ob.get(4))
