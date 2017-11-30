#!python
"""Python implementatin of HashTable."""

from linkedlist import LinkedList


class HashTable(object):
    """HashTable object that holds data that can be quickly retrieved.

    Attributes:
        buckets: A list of LinkedLists that will hold the data

    """

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def __getitem__(self, key):
        """Return the value for the given key."""
        return self.get(key)

    def __setitem__(self, key, value):
        """Return the value for the given key."""
        return self.set(key, value)

    def __iter__(self):
        """Return iter of all ht buckets list."""
        return iter(self.buckets)

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.

        Performance:
            Best and worse case O(n^2), because it has to loop through the
                whole buckets list and the buckets.items() list
        """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, _ in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.

        Performance:
            Best and worse case O(n^2), because it has to loop through all the
                buckets of the HashTable and all the items of each bucket
        """
        all_values = []
        for bucket in self.buckets:
            for _, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all key-value pairs in this hash table.

        Performance:
            Best and worse case O(n), because it has to loop through all the
                buckets in the HashTable
        """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())

        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.

        Performance:
            Best and worse case O(1) because size is a saved variable that's
                instantly retrieved
        """
        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.

        Performance:
            Best and worse case O(n^2), because it has to loop through the
                whole buckets list and the buckets.items() (to get keys)
                before it can check if the key is within the HashTable
        """
        return key in self.keys()

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.

        Performance:
            Best O(1), if key is in the first position of the first bucket
            Worst O(n^2), if key is at the very end of the HashTable
        """
        for bucket in self.buckets:
            for bucket_key, bucket_value in bucket.items():
                if bucket_key == key:
                    return bucket_value

        raise KeyError('The key "{}" was not found'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.

        Performance:
            Best O(1), if it's an unique key, or if the HashTable is empty
            Worst O(n), if key is at the very end of the bucket (if replacing)
        """
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        new_item = (key, value)

        try:
            item = (key, self.get(key))
        except KeyError:
            bucket.append(new_item)
            self.size += 1
            return

        bucket.replace(item, new_item)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.

        Performance:
            Best O(1), if the key is the first in the HashTable
            Worst O(n), if key is at the very end of the bucket, or if the key
                is not found.
        """
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        item = (key, self.get(key))  # Throws KeyError

        bucket.delete(item)
        self.size -= 1


def test_hash_table():
    """Test the functionality of the HashTable implementation."""
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting set twice(update):')
    for key, value in [('I', 2), ('V', 10), ('X', 20)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))

    print('\nTesting iteration:')
    for item in ht:
        print(item)

    print('\nTesting subscritping:')
    for key in ['I', 'V', 'X']:
        print('ht[{!r}]: {!r}'.format(key, ht[key]))
        print('Test set item...')
        ht[key] = '{} {} {}'.format(key, key, key)
        print('ht[{!r}] is now {!r}'.format(key, ht[key]))


if __name__ == '__main__':
    test_hash_table()
