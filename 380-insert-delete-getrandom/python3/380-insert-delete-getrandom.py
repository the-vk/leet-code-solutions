from random import random

class RandomizedSet:

  def __init__(self):
    self.m = 1024
    self.buckets = [None] * self.m
    self.buckets_list = []
    self.count = 0

  def insert(self, val: int) -> bool:
    h = self.hash(val)
    if None == self.buckets[h]:
      self.buckets[h] = []
      self.buckets_list.append(h)
    for v in self.buckets[h]:
      if v == val:
        return False
    self.buckets[h].append(val)
    self.count += 1
    return True

  def remove(self, val: int) -> bool:
    h = self.hash(val)
    if None == self.buckets[h]:
      return False
    for vi in range(len(self.buckets[h])):
      if self.buckets[h][vi] == val:
        self.buckets[h].pop(vi)
        self.count -= 1
        if len(self.buckets[h]) == 0:
          self.buckets[h] = None
          self.buckets_list.remove(h)
        return True
    return False

  def getRandom(self) -> int:
    if self.count < 1:
      raise "No Elements"
    bi = self.buckets_list[int(random() * len(self.buckets_list))]
    ii = int(random() * len(self.buckets[bi]))
    return self.buckets[bi][ii]
        
  def hash(self, val) -> int:
    return val % self.m


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()