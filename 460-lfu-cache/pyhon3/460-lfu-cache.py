from math import floor

class LFUCache:

    def __init__(self, capacity: int):
        # node: [key, value, counter, heap_index]
        # min-heap: counter is key
        self.capacity = capacity
        self.heap = [None] * self.capacity
        self.map = {}

    def get(self, key: int) -> int:
        print(f"get({key}: {self.heap})")
        if key in self.map:
            node = self.map[key]
            self.inc(node)
            print(f"get{self.heap})")
            return node[1]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        print(f"put({key}={value}: {self.heap})")
        if key in self.map:
            node = self.map[key]
            self.inc(node)
            node[1] = value
        else:
            if self.capacity == 0:
                del self.map[self.heap[0][0]]
                self.swap(0, len(self.heap) - 1)
                self.heap[-1] = None
                self.down_heapify(0)
                self.capacity = 1
            index = len(self.heap) - self.capacity
            node = [key, value, 1, index]
            self.heap[index] = node
            self.map[key] = node
            self.capacity -= 1
            self.up_heapify(index)
        print(f"put: {self.heap})")

        
    def inc(self, node) -> None:
        node[2] += 1
        self.down_heapify(node[3])

    def down_heapify(self, i) -> None:
        print(f"down {i}: {self.heap}")
        left = i * 2 + 1
        right = i * 2 + 2
        smallest = i

        if left < len(self.heap) and self.heap[left] != None and self.heap[left][2] < self.heap[smallest][2]:
            smallest = left

        if right < len(self.heap) and self.heap[right] != None and self.heap[right][2] < self.heap[smallest][2]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.down_heapify(smallest)
    
    def up_heapify(self, i) -> None:
        print(f"up ({i}): {self.heap}")
        if i == 0:
            return
        parent = floor((i - 1) / 2)
        if self.heap[i][2] < self.heap[parent][2]:
            self.swap(i, parent)
            self.up_heapify(parent)

    def swap(self, l, r) -> None:
        node_l = self.heap[l]
        self.heap[l] = self.heap[r]
        self.heap[l][3] = l
        self.heap[r] = node_l
        self.heap[r][3] = r
        

         


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)