




from threading import RLock

class ConcurrentMyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket_size = 1000  # Define the number of buckets
        # Initialize buckets list of lists to handle collisions via chaining
        self.buckets = [[] for _ in range(self.bucket_size)]
        # Initialize a re-entrant lock for each bucket to ensure thread safety
        self.locks = [RLock() for _ in range(self.bucket_size)]

    def _hash(self, key: int) -> int:
        """
        Generate a hash for the given key. For simplicity, using modulo operator.
        """
        return key % self.bucket_size

    def _contains(self, key: int, hash_key: int) -> bool:
        """
        Helper method to check if the hash set contains the specified element without acquiring the lock.
        This is used to avoid redundant locking.
        """
        return key in self.buckets[hash_key]

    def add(self, key: int) -> None:
        """
        Add a key to the hash set, in a thread-safe manner.
        """
        hash_key = self._hash(key)
        with self.locks[hash_key]:  # Using re-entrant lock
            if not self._contains(key, hash_key):
                self.buckets[hash_key].append(key)

    def remove(self, key: int) -> None:
        """
        Remove a key from the hash set, if it exists, in a thread-safe manner.
        """
        hash_key = self._hash(key)
        with self.locks[hash_key]:  # Using re-entrant lock
            if self._contains(key, hash_key):
                self.buckets[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if the hash set contains the specified element, in a thread-safe manner.
        """
        hash_key = self._hash(key)
        with self.locks[hash_key]:  # Using re-entrant lock
            return self._contains(key, hash_key)

# Demonstration of ConcurrentMyHashSet functionality

#######################################################################################
























