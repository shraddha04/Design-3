class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    # TC : O(1)
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        node = self.map[key]
        self.removeNode(node)
        self.addToHead(node)
        return node.value

    # TC : O(1)
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.map:
            node = self.map[key]
            node.value = value
            self.removeNode(node)
            self.addToHead(node)
        else:
            if len(self.map) >= self.capacity:
                tail = self.tail.prev
                self.removeNode(tail)
                del self.map[tail.key]

            node = Node(key, value)
            self.map[key] = node
            self.addToHead(node)