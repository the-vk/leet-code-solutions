class PeekingIterator:
  def __init__(self, iterator):
    self.iterator = iterator
    self.item = None

  def peek(self):
    if self.item == None:
      self.item = self.iterator.next()
    return self.item

  def next(self):
    tmp = None
    if self.item:
      tmp = self.item
    else:
      tmp = self.iterator.next()
    self.item = None
    return tmp

  def hasNext(self):
    return self.item != None or self.iterator.hasNext()
