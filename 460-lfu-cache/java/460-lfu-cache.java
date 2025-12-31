class LFUCache {
  class Item {
    int key;
    int value;
    int usage;
    int access;

    Item(int key, int value) {
      this.key = key;
      this.value = value;
      this.usage = 0;
      this.access = 0;
    }
  }

  class ItemPointer implements Comparable<ItemPointer> {
    int key;
    int usage;
    int access;

    ItemPointer(int key, int usage, int access) {
      this.key = key;
      this.usage = usage;
      this.access = access;
    }

    @Override
    public int compareTo(ItemPointer r) {
      if (this.usage < r.usage) {
        return -1;
      }

      if (this.usage > r.usage) {
        return 1;
      }

      if (this.access < r.access) {
        return -1;
      }

      if (this.access > r.access) {
        return 1;
      }

      return 0;
    }
  }

  int capacity;
  int counter;
  Map<Integer, Item> storage;
  PriorityQueue<ItemPointer> evictionQueue;

    public LFUCache(int capacity) {
      this.capacity = capacity;
      this.counter = 0;
      this.storage = new HashMap<>();
      this.evictionQueue = new PriorityQueue<>();
    }
    
  public int get(int key) {
    if (this.storage.containsKey(key)) {
      var item = this.storage.get(key);
      this.incUsage(item);
      return item.value;
    }
    return -1;
  }
    
  public void put(int key, int value) {
    if (this.storage.containsKey(key)) {
      var item = this.storage.get(key);
      item.value = value;
      this.incUsage(item);
    } else {
      this.evictIfNecessary();
      var item = new Item(key, value);
      this.storage.put(key, item);
      this.incUsage(item);
    }
  }

  private void incUsage(Item item) {
    item.usage++;
    item.access = ++this.counter;

    var pointer = new ItemPointer(item.key, item.usage, item.access);
    this.evictionQueue.add(pointer);
  }

  private void evictIfNecessary() {
    if (this.storage.size() < this.capacity) {
      return;
    }

    while (!this.evictionQueue.isEmpty()) {
      var tip = this.evictionQueue.peek();
      var item = this.storage.get(tip.key);
      if (tip.usage != item.usage || tip.access != item.access) {
        this.evictionQueue.poll();
      } else {
        break;
      }
    }

    var victim = this.evictionQueue.poll();
    this.storage.remove(victim.key);
  }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
