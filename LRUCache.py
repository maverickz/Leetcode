from llist import dllist, dllistnode
import logging
import sys
import copy
from collections  import namedtuple

logging.basicConfig(stream = sys.stderr)
logging.getLogger("LRUCache_log").setLevel(logging.DEBUG)
log = logging.getLogger("LRUCache_log")

Node = namedtuple('Node', 'key val')

class Cache(object):
    def __init__(self, logger = None, size = 2):
        log = logger
        self._size = size
        self._hash_map = {}
        self._queue = dllist()

    @property 
    def size(self):
        # Get the current hash size
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property 
    def hash_map(self):
        # Get the current hash size
        return self._hash_map

    @property 
    def queue(self):
        # Get the current hash size
        return self._queue

    def display_cache(self):
        output = "Hashmap" + str(self._hash_map) + "_queue" + str(self._queue)
        log.debug("Hashmap: %s, _queue: %s" % (self._hash_map, self._queue))

    def cache_size(self):
        """
        Returns the number of entries currently in the cache
        """
        return len(self._hash_map)

    def is_cache_full(self):
        return self.cache_size() == self.size

    def add(self, key, value):
        """
        Add a Page identified by the key, value pair in the cache

        """
        # If the key already exists in the _hash_map move the node to the 
        # front of the _queue and return
        if key in self._hash_map:
            self.get(key)
            return

        # If the cache is full, remove the first node in the _queue i.e
        # the least referred node in the _queue and delete the corresponding
        # entry in _hash_map
        if self.is_cache_full():
            old_node = self._queue.popleft()
            old_node_key = old_node.key
            del self._hash_map[old_node_key]

        # Append the new node to the front of the queue and insert the list node
        # object in the hash_map, so that the list node can be removed/deleted
        # without the need for it's index in the list
        # Note: 
        # node: <class 'LRUCache.Node'>
        # dlnode: <type 'llist.dllistnode'>
        #
        node = Node(key, value)
        self._queue.appendright(node)
        dlnode = self._queue.last
        self._hash_map[key] = dlnode

    def get(self, key):
        """
        Return the Page identified by the key, value pair if it exists in the cache

        """
        # If key exists in the hash_map return the node after updating its position
        # in the queue i.e move it to the front of the queue
        if key in self._hash_map:
            dlnode = self._hash_map[key]
            node = dlnode.value
            new_node = Node(node.key, node.val)
            self._queue.remove(dlnode)
            # A new node is inserted as the old node has been removed from the queue
            self._queue.appendright(new_node)
            new_dlnode = self._queue.last
            # Update the new node in the hash_map
            self._hash_map[key] = new_dlnode
            return new_node.val
        else:
            return None

    def peek(self, key):
        """
        Test utility function
        Checks if a key exists in the hash_map
        """
        if key in self._hash_map:
            return True
        else:
            return False







    

