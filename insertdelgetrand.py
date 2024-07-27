import random
class RandomizedSet(object):

    def __init__(self):
        self.data = []
        self.index_map = {}

    def insert(self, val):
        if val in self.index_map:
            return False
        self.data.append(val)
        self.index_map[val] = len(self.data)-1
        return True
    def remove(self, val):
        if val not in self.index_map:
            return False
        index  = self.index_map[val]
        last_ele = self.data[-1]
        self.data[index] = last_ele
        self.index_map[last_ele]= index
        self.data.pop()
        del self.index_map[val]
        return True

    def getRandom(self):
        if not self.data:
            return None
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

