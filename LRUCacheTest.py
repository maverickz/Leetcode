import unittest
import logging
import sys
import random
import LRUCache

log = logging.getLogger()
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
log.addHandler(ch)

class CacheTest(unittest.TestCase):
    cache = None
    log = None
    cache_size = 2
    max_cache_size = 10

    def setUp(self):
        self.cache = LRUCache.Cache(log, self.cache_size)

    def test_add_empty_cache(self):
        if self.cache:
            key = 1
            value = 10
            self.cache.add(key,value)
            self.cache.display_cache()
            self.assertEqual(self.cache.get(key),value)
            self.assertEqual(self.cache.cache_size(), 1)

    def test_multiple_add(self):
        if self.cache:
            keys = [2, 1]
            values = [20, 10]
            for key, value in zip(keys,values):
                self.cache.add(key,value)
                self.assertEqual(self.cache.get(key),value)

            self.cache.display_cache()
            for key, value in zip(keys,values):
                self.assertEqual(self.cache.get(key),value)
        else:
            log.error("Cache is NULL")

    def test_duplicate_add(self):
        if self.cache:
            keys = [1, 1, 2, 1]
            values = [10, 10, 20, 10]
            for key, value in zip(keys,values):
                self.cache.add(key,value)
                self.assertEqual(self.cache.get(key),value)

            self.cache.display_cache()
            for key, value in zip(keys,values):
                self.assertEqual(self.cache.get(key),value)
        else:
            log.error("Cache is NULL")

    def test_get_empty_cache(self):
        if self.cache:
            key = 1
            self.cache.display_cache()
            self.assertEqual(self.cache.get(key),None)
        else:
            log.error("Cache is NULL")

    def test_multiple_duplicate_add(self):
        if self.cache:
            key = 1
            value = 10
            curr_cache_size = self.cache.cache_size()
            loop = self.cache.size
            for _ in xrange(loop):
                self.cache.add(key,value)

            new_cache_size = self.cache.cache_size()    
            self.assertEqual(curr_cache_size+1,new_cache_size)

        else:
            log.error("Cache is NULL")

    def test_set_cache_size(self, cache_size = None):
        if self.cache:
            if not cache_size:
                self.cache_size = cache_size
            else:
                self.cache_size = random.randint(0,self.max_cache_size)
            self.cache.size = self.cache_size
            self.assertEqual(self.cache.size, self.cache_size)
        else:
            log.error("Cache is NULL")


    def test_add_full_cache(self):
        if self.cache:
            key_start = 0
            val_start= 100
            num_entries = 10
            set_cache_size = 5

            test_set_cache_size(set_cache_size)
            for key, value in zip(xrange(key_start,key_start+num_entries), xrange(val_start,val_start+num_entries)):
                self.cache.add(key,value)

            new_cache_size = self.cache.cache_size()    
            self.assertEqual(set_cache_size,new_cache_size)
   
            self.assertEqual(set_cache_size,new_cache_size)

        else:
            log.error("Cache is NULL")

if __name__ =='__main__':
    unittest.main()