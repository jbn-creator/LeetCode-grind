from random import randint
class RandomizedSet:

    def __init__(self):
        self.randomSet = dict()

    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        else:
            self.randomSet[val] = "insert"
            return True

    def remove(self, val: int) -> bool:
        if val in self.randomSet:
            del self.randomSet[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        arrayRS = list(self.randomSet.keys())
        random = randint(0,(len(arrayRS) - 1))
        return arrayRS[random]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()