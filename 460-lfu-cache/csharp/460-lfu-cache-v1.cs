using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

public class LFUCache {
    private class CacheEntry
    {
        public int key;
        public int value;
        public int counter;
        public CacheEntry prev;
        public CacheEntry next;
    }
    
    private class CacheList
    {
        private CacheEntry root;
        
        public bool Empty => root.next == root && root.prev == root;
        
        public CacheList()
        {
            root = new CacheEntry();
            root.prev = root;
            root.next = root;
        }
        
        public void Push(CacheEntry node)
        {
            node.next = root.next;
            node.prev = root;
            node.next.prev = node;
            root.next = node;
        }
        
        public CacheEntry Pop(CacheEntry node = null)
        {
            if (Empty) return null;
            
            if (node == null) node = root.prev;
            
            node.next.prev = node.prev;
            node.prev.next = node.next;
            node.next = null;
            node.prev = null;
            return node;
        }
    }
    
    Dictionary<int, CacheEntry> keyStorage;
    Dictionary<int, CacheList> counterStorage;
    int minCounter = 0;
    int capacity;

    public LFUCache(int capacity) {
        this.keyStorage = new Dictionary<int, CacheEntry>();
        this.counterStorage = new Dictionary<int, CacheList>();
        counterStorage[1] = new CacheList();
        this.capacity = capacity;
    }
    
    public int Get(int key) {
        if (keyStorage.ContainsKey(key)) {
            var node = keyStorage[key];
            IncCounter(node);
            return node.value;
        } else {
            return -1;
        }
    }
    
    public void Put(int key, int value) {
        if (capacity == 0) return;
        if (keyStorage.ContainsKey(key)) {
            var node = keyStorage[key];
            node.value = value;
            IncCounter(node);
        }
        else
        {
            if (keyStorage.Count == capacity) {
                var expireItem = counterStorage[minCounter].Pop();
                keyStorage.Remove(expireItem.key);
            }
            var node = new CacheEntry()
            {
                key = key,
                value = value,
                counter = 1
            };
            minCounter = 1;
            counterStorage[node.counter].Push(node);
            keyStorage[node.key] = node;
        }   
    }
    private void IncCounter(CacheEntry node)
    {
        counterStorage[node.counter].Pop(node);
        if (counterStorage[node.counter].Empty && minCounter == node.counter) {
            minCounter++;
        }
        node.counter++;
        if (counterStorage.ContainsKey(node.counter)) {
            counterStorage[node.counter].Push(node);
        } else {
            counterStorage[node.counter] = new CacheList();
            counterStorage[node.counter].Push(node);
        }
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */

public static class Program
{
    public static void Main()   
    {
        var cache = new LFUCache(2);
        cache.Put(1,1);
        cache.Put(2,2);
        var value = cache.Get(1);
        cache.Put(3,3);
        value = cache.Get(2);
        value = cache.Get(3);
        cache.Put(4,4);
        value = cache.Get(1);
        value = cache.Get(3);
        value = cache.Get(4);
    }

    // private static void Test(int expected, int[][] dominoes)
    // {
    //     var solution = new Solution();
    //     var stopwatch = Stopwatch.StartNew();
    //     var actual = solution.NumEquivDominoPairs(dominoes);
    //     if (actual != expected)
    //     {
    //         Console.WriteLine($"actual value '{actual}' is not equal to expected value '{expected}'");
    //     }
    //     stopwatch.Stop();
    //     var elapsed = stopwatch.Elapsed.TotalSeconds;
    //     Console.WriteLine($"elapsed: {elapsed} secs");
    // }
}
