class TrieNode:
  def __init__(self):
    self.children = [None]*26
    self.isEndOfWord = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str) -> None:
    node = self.root
    for x in word:
      v = ord(x) - ord('a')
      if node.children[v] == None:
        node.children[v] = TrieNode()
      node = node.children[v]
    node.isEndOfWord = True

  def search(self, word: str) -> bool:
    node = self.root
    for x in word:
      v = ord(x) - ord('a')
      if node.children[v] == None:
        return False
      node = node.children[v]
    return node.isEndOfWord
        

  def startsWith(self, prefix: str) -> bool:
    node = self.root
    for x in prefix:
      v = ord(x) - ord('a')
      if node.children[v] == None:
        return False
      node = node.children[v]
    return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)