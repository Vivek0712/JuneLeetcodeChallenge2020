from random import choice

class RandomizedSet:

    def __init__(self):
        self.ds = []
        self.hm = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.hm:
            ind = len(self.ds)
            self.ds.append(val)
            self.hm[val] = ind
            return True
        return False


    def remove(self, val: int) -> bool:
        
        if val in self.hm:
            ind = self.hm[val]
            lastele = self.ds[-1]
            self.ds[ind] = lastele
            self.hm[lastele] = ind
            del self.hm[val]
            self.ds.pop()
            return True
        return False
        

    def getRandom(self) -> int:

        return choice(self.ds)  