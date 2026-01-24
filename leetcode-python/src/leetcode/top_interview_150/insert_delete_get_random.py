class RandomizedSet(object):

    def __init__(self):
        import random

        self.r = random.choice
        self.arr = []
        self.hmap = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.arr:
            return False
        self.arr.append(val)
        self.hmap[val] = len(self.arr) - 1

        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.arr:
            return False

        index = self.hmap[val]
        last_index = len(self.arr) - 1

        if index < last_index:
            self.arr[index], self.arr[last_index] = (
                self.arr[last_index],
                self.arr[index],
            )
            self.hmap[self.arr[index]] = index

        self.arr.pop(last_index)
        del self.hmap[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return self.r(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
