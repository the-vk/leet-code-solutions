import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;

public class Codec {
  private final static String BASE_URL = "https://tinyurl.com/";

  private AtomicLong counter;
  private final Map<String, String> storage;
  private final Map<String, String> reverseStorage;

  public Codec() {
    this.counter = new AtomicLong(0);
    this.storage = new ConcurrentHashMap<>();
    this.reverseStorage = new ConcurrentHashMap<>();
  }

  // Encodes a URL to a shortened URL.
  public String encode(String longUrl) {
    if (this.reverseStorage.containsKey(longUrl)) {
      return this.formatUrl(this.reverseStorage.get(longUrl));
    }

    return this.formatUrl(this.reverseStorage.computeIfAbsent(longUrl, url -> {
      var key = Long.toString(this.counter.getAndIncrement(), 36);
      this.storage.put(key, url);
      return key;
    }));
  }

  // Decodes a shortened URL to its original URL.
  public String decode(String shortUrl) {
    var key = shortUrl.substring(BASE_URL.length());
    return this.storage.getOrDefault(key, null);
  }

  private String formatUrl(String key) {
    return String.format("%s%s", BASE_URL, key);
  }
}