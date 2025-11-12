from random import randint
class RandomizedSet:

    def __init__(self):
        self.randomArr = []
        self.randomSet = dict()
        self.currentIndex = 0

    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        else:
            self.randomArr.append(val)
            self.randomSet[val] = self.currentIndex
            self.currentIndex += 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.randomSet:
            swappedEl = self.randomArr[-1]
            self.randomArr[-1] = val
            self.randomSet[swappedEl] = self.randomSet[val]
            self.randomArr[self.randomSet[val]] = swappedEl
            self.randomArr.pop()
            self.currentIndex -= 1
            del self.randomSet[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        random = randint(0,(len(self.randomArr) - 1))
        return self.randomArr[random]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()