class TrieNode:
  def __init__(self):
    self.children = [None]*26
    self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
      self.root = TrieNode()        

    def addWord(self, word: str) -> None:
      node = self.root
      for x in word:
        v = ord(x) - ord('a')
        if node.children[v] == None:
          node.children[v] = TrieNode()
        node = node.children[v]
      node.isEndOfWord = True
        

    def search(self, word: str) -> bool:  
      return self.searchNode(word, 0, self.root)    
      

    def searchNode(self, word, i, node):
      if i == len(word):
        return node.isEndOfWord
      
      l = word[i]
      ns = []
      if l == '.':
        for x in node.children:
          if x != None:
            ns.append(x)
      else:
        x = node.children[ord(l) - ord('a')]
        if x != None:
          ns.append(x)
      if len(ns) == 0:
        return False
      ans = False
      for n in ns:
        ans = ans or self.searchNode(word, i + 1, n)
      return ans
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)