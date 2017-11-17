"""This module contains two data models related to histograms."""
import random


class Dictogram(dict):
    """Histogram data model constructed as a dictionary."""

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items."""
        super(Dictogram, self).__init__()

        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram

        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable."""
        for item in iterable:
            if item not in self:
                self[item] = 0
                self.types += 1

            self[item] += 1
            self.tokens += 1

    def count(self, item):
        """Return the count of the given item in this histogram, or 0."""
        if item not in self:
            return 0

        return self[item]

    def get_random_word(self):
        """Return a random word."""
        random_key = random.sample(self, 1)
        return random_key[0]

    def get_weighted_random_word(self):
        """Return a random word using weights."""
        random_int = random.randint(0, self.tokens - 1)
        index = 0
        list_of_keys = list(self)

        for i in range(0, self.types):
            index += self[list_of_keys[i]]

            if(index > random_int):

                return list_of_keys[i]


class Listogram(list):
    """Histogram data model constructed as a list of lists."""

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items."""
        super(Listogram, self).__init__()

        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram

        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable."""
        for item in iterable:
            if not self.__contains__(item):
                self.append([item, 0])
                self.types += 1

            self[self._index(item)][1] += 1
            self.tokens += 1

    def count(self, item):
        """Return the count of the given item in this histogram, or 0."""
        for word, freq in self:
            if item == word:
                return freq

        return 0

    def __contains__(self, item):
        """Return True if the given item is in this histogram, or False."""
        return item in [word for word, freq in self]

    def _index(self, target):
        """Return the index of the (target, count) entry if found, or None."""
        return self.index([target, self.count(target)])


def test_histogram(text_list):
    """Test the functinality of both histogram data models."""
    print('text list:', text_list)

    hist_dict = Dictogram(text_list)
    print('dictogram:', hist_dict)

    hist_list = Listogram(text_list)
    print('listogram:', hist_list)


def read_from_file(filename):
    """Parse the given file into a list of strings, separated by seperator."""
    return open(filename, 'r').read().strip().split()


if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]  # exclude script name in first argument

    if len(arguments) == 0:
        # test hisogram on letters in a word
        word = 'abracadabra'
        test_histogram(word)
        print()
        # test hisogram on words in a sentence
        sentence = 'one fish two fish red fish blue fish'
        word_list = sentence.split()
        test_histogram(word_list)

    elif len(arguments) == 1:
        # test hisogram on text from a file
        filename = arguments[0]
        text_list = read_from_file(filename)
        test_histogram(text_list)

    else:
        # test hisogram on given arguments
        test_histogram(arguments)
