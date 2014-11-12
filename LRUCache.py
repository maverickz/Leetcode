from llist import dllist
import unittest
import logging
import sys


class LRUCache:
    def __init__(self, log = None, size=2):
        logging.basicConfig(stream = sys.stderr)
        logging.getLogger("LRUCache_log").setLevel(logging.DEBUG)
        _log = logging.getLogger("LRUCache_log")
        _log.debug("LOG WORKS")
        self._size = size
        hash_map = {}
        queue = dllist()

    @property 
    def size(self):
        # Get the current hash size
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property 
    def log(self):
        # Get the current hash size
        return self._log

    def display_cache(self):
        output = "Hashmap" + str(self.hash_map) + "Queue" + str(queue)
        log.debug("%s" % output)
        return "OUTPUT"

    def is_cache_full(self):
        return len(self.hash_map) == self.size

    def add(self, key, value):
        logging.basicConfig(stream = sys.stderr)
        logging.getLogger("LRUCache_log").setLevel(logging.DEBUG)
        log = logging.getLogger("LRUCache_log1")
        log.debug("But not here")
        if key in self.hash_map:
            self.get(key)
            return
        if is_cache_full():
            old_node_key = self.queue.popleft()
            del self.hash_map[old_node_key]

        self.hash_map[key] = value
        self.queue.appendright(key)

    def get(self, key):
        if key in self.hash_map:
            self.queue.remove(key)
            self.queue.appendright(key)
            return node
        else:
            return None

class BasicTest(unittest.TestCase):
    cache = None
    log = None

    def setUp(self):
        cache = LRUCache()
        logging.basicConfig(stream = sys.stderr)
        self.log = logging.getLogger("LRUCacheTest_log")

        self.log.setLevel(logging.DEBUG)
         
        

    def test_simple_add(self):
        if self.cache:
            key = 1
            value = 10
            cache.add(key,value)
            cache.display_cache()
            self.assertEqual(cache.get(key),value)

    def test_multiple_add(self):
        if self.cache:
            keys = [2, 1]
            values = [20, 10]
            for key, value in zip(keys,values):
                cache.add(key,value)
                self.assertEqual(cache.get(key),value)
            
            print "Hello"
            self.log.debug(cache.display_cache())
            for key, value in zip(keys,values):
                self.assertEqual(cache.get(key),value)

if __name__ =='__main__':
    logging.basicConfig(stream = sys.stderr)
    logging.getLogger("LRUCache").setLevel(logging.DEBUG)
    unittest.main()






    

