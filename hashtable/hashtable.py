class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        """Print entire linked list."""
        if self.head is None:
            return "[Empty List]"

        cur = self.head
        s = ""

        while cur != None:
            s += f"({cur.value})"

            if cur.next is not None:
                s += "-->"

            cur = cur.next
        return s

    def find(self, value):
        cur = self.head

        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next

        return None

    def delete(self, key):
        cur = self.head

        # Special case of deleting head​

        if cur.key == key:
            self.head = cur.next
            return cur

        # General case of deleting internal node
        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.key == key:  # Found it!
                prev.next = cur.next  # Cut it out
                return cur  # Return deleted node
            else:
                prev = cur
                cur = cur.next

        return None  # If we got here, nothing found

    def insert_at_head(self, node):

        node.next = self.head
        self.head = node

    def insert_or_overwrite_value(self, key, value):
        node = self.find(value)

        if node is None:
            # Make a new node
            self.insert_at_head(HashTableEntry(key, value))

        else:
            # Overwrite old value
            node.value = value


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.buckets = []
        self.load_factor = 0.7

        self.init_buckets(capacity)

    def init_buckets(self, capacity):
        self.buckets = [None] * capacity

        for i in range(capacity):
            self.buckets[i] = LinkedList()

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.load_factor

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = ((hash << 5) + hash) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        index = self.hash_index(key)

        self.buckets[index].insert_or_overwrite_value(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        deletedEntry = self.buckets[index].delete(key)

        if deletedEntry is None:
            print("Can't delete. No value at this key.")
        else:
            return deletedEntry

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        cur = self.buckets[index].head

        while cur is not None:
            if key == cur.key:
                return cur.value

            cur = cur.next

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity

        hashEntries = []

        for entry in self.buckets:
            if entry.head is not None:
                cur = entry.head

                while cur is not None:
                    hashEntries.append(cur)
                    cur = cur.next

        self.init_buckets(new_capacity)

        for entry in hashEntries:
            index = self.hash_index(entry.key)
            self.buckets[index].insert_or_overwrite_value(entry.key, entry.value)
            print(self.buckets[index])


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")
    ht.put("key-9", "val-9")

    ht.resize(1024)

    return_value = ht.get("key-0")
    print(return_value)
    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    # print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
