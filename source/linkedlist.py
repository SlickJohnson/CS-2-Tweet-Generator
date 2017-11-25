"""LinkedList python implementation."""


class Node(object):
    """Node object for LinkedLists.

    Attributes:
        data: A variable containing any datatype
        next: A variable that poitns to the next node in a ll

    """

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):
    """LinkedList object containing a list of nodes.

    head(Node): First node in linked list.
    tail(Node): Last node in inked list.
    """

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.

        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item.
        """
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.

        Best and worst case running time: O(n) because we always need to loop
        through all n nodes get the length.
        """
        if self.head is None:
            return 0

        if self.head == self.tail:
            return 1

        return len(self.items())

    def append(self, item):
        """Insert the given item at the tail of this linked list.

        Args:
            item: A variable that is of any datatype

        Result:
            A new node is created to hold item and is connected to the tail
            node. If the ll is empty, the new node is set to the head of the ll
            in order to start a new ll.

        """
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.

        Args:
            item: A variable that is of any datatype

        Result:
            A new node is created to hold item and is connected to the head
            node. If the ll is empty, the head and tail become the new node.
            If the ll has only one node (head == tail), the head becomes
            the newly created node and it's connected to the tail node.

        """
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        elif self.tail == self.head:
            self.head = new_node
            self.head.next = self.tail
        else:
            old_node = self.head  # Keep track of old head to prevent overwrite
            self.head = new_node
            self.head.next = old_node

    def find(self, quality):
        """Return an item from ll satisfying the given quality.

        Args:
            quality: A variable that determines the quality of an item
                returning True if the quality matches and False otherwise.

        Returns:
            A the data of a node that matches the quality provided.

        """
        # TODO: Best case running time: O(???) Why and under what conditions?
        # TODO: Worst case running time: O(???) Why and under what conditions?
        if self.is_empty():  # Ll is empty, so return nothing
            return None

        current_node = self.head
        while current_node:  # Loop until None
            if quality(current_node.data):  # If quality(item) is true,
                return current_node.data  # Return item

            current_node = current_node.next

        return None  # Return None if quality was not satisfied

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.

        Best case running time: O(1) if item is first in ll
        """
        # TODO: Worst case running time: O(n-1) if item is second to last
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    """Run simple tests to check if the linkedlist object works."""
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    print('\nTesting prepending:')
    for item in ['A', 'B', 'C']:
        print('prepend({!r})'.format(item))
        ll.prepend(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
