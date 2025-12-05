class LRUCache {
    private LinkedHashMap<Integer, Integer> storage;

    public LRUCache(int capacity) {
      this.storage = new LinkedHashMap<Integer, Integer>(16, 0.75f, true) {
        @Override
        protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
          return size() > capacity;
        }
      };
    }

    public int get(int key) {
      return this.storage.getOrDefault(key, -1);
    }

    public void put(int key, int value) {
      this.storage.put(key, value);
    }
  }