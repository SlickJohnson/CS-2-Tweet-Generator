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

    Attributes:
        head: The first node in the list
        tail: The last node in the list
        size: An int that tracks the length of the list

    """

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
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

        Performance:
            O(1) because length is a stored variable that increments/decrements
                based on the ll functions used.
        """
        return self.size

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
        self.size += 1

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

        self.size += 1

    def find(self, quality):
        """Return an item from ll satisfying the given quality.

        Args:
            quality: A variable that determines the quality of an item
                returning True if the quality matches and False otherwise.

        Returns:
            A the data of a node that matches the quality provided.

        """
        if self.is_empty():  # Ll is empty, so return nothing
            return ValueError("Linkedlist is empty")

        current_node = self.head
        while current_node:  # Loop until None
            if quality(current_node.data):  # If quality(item) is true,
                return current_node.data  # Return item

            current_node = current_node.next

        return None  # Return None if quality was not satisfied

    def delete(self, item):
        """Delete the given item from this ll, or raise ValueError.

        Result:
            The first matching node is forgotten by taking the previous node's
            next variable and setting it to the matching node's next variable.
            The result is a ll that has no access to the 'deleted' node.

        Performance:
            O(1) if item is first in ll
            O(n) if item is last in ll

        """
        if self.is_empty():
            raise ValueError("Item not found: {}. Empty list.".format(item))

        if self.head.data == item:
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.head = None
                self.tail = None
            return

        current_node = self.head
        prev_node = current_node
        while current_node:  # Loop until None
            if current_node.data == item:
                self.size -= 1

                if self.size == 0:
                    self.head = None
                    self.tail = None
                    return

                if self.tail == current_node:
                    self.tail = prev_node
                    return

                prev_node.next = current_node.next  # Forget the node
                return

            prev_node = current_node
            current_node = current_node.next

        raise ValueError("Item not found: {}".format(item))


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
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('delete({!r})'.format("x"))
        ll.delete("x")
        print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
