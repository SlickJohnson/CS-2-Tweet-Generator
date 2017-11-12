class MarkovChain(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(MarkovChain, self).__init__()

        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram

        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for i in range(0, len(iterable)):
            if

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        if item not in self:
            return 0

        return self[item]
