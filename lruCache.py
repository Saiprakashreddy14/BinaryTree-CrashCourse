from collections import OrderedDict

class lruCache :
    def __init__(self,capacity=3):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self,key):
        if key not in self.cache:
            return -1
        val = self.cache.get(key)
        self.cache.move_to_end(key)
        return val


    def put(self,key,val):
        if key in self.cache:
            del self.cache[key]
        self.cache[key]=val
            



