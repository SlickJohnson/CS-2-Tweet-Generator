"""Classes of different order Markov Chains."""
import random
from histograms import Dictogram


class FirstOrderMarkovChain(dict):
    """Implementation of a first order markov chain."""

    def __init__(self, iterable=None):
        """Initialize this as a Python dictionary and update if iterable provided."""
        super(FirstOrderMarkovChain, self).__init__()

        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update the data within the model.

        Args:
            iterable: Any iterable type (preferably a word list)
        """
        len_of_iterable = len(iterable)  # O(1)

        for i in range(0, len_of_iterable - 1):  # O(n) n = length of iterable
            if iterable[i] not in self:
                self[iterable[i]] = Dictogram()

            self[iterable[i]].update([iterable[i + 1]])  # O(1) updating dict

    def generate_sentence(self, length):
        """Return a sentence generated using a markov_chain."""
        current_word = random.choice(list(self))
        sentence = [current_word]

        for _ in range(0, length):
            current_dictogram = self[current_word]
            random_weighted_word = current_dictogram.get_weighted_random_word()
            current_word = random_weighted_word
            sentence.append(current_word)

        sentence[0] = sentence[0].capitalize()

        return ' '.join(sentence) + '.'


class SecondOrderMarkovChain(dict):
    """Implementation of a first order markov chain."""

    def __init__(self, iterable=None):
        """Initialize this as a Python dictionary and update if iterable provided."""
        super(SecondOrderMarkovChain, self).__init__()

        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update the data within the model.

        Args:
            iterable: Any iterable type (preferably a word list)
        """
        for i in range(0, len(iterable) - 2):
            key = tuple(iterable[i: i + 2])

            if key not in self:
                self[key] = Dictogram()

            self[key].update([iterable[i + 2]])

    def generate_sentence(self, length):
        """Return a sentence generated using a markov_chain."""
        current_window = random.choice(list(self))
        sentence = [current_window[1]]

        for _ in range(0, length):
            try:
                current_dictogram = self[current_window]
                random_weighted_word = current_dictogram.get_weighted_random_word()
                current_window = (current_window[1], random_weighted_word)
                sentence.append(random_weighted_word)
            except KeyError:
                break

        sentence[0] = sentence[0].capitalize()
        return ' '.join(sentence) + '.'


def test_markov_chain(word_list):
    """Test the functinality of markov chain."""
    markov_chain = FirstOrderMarkovChain(word_list)
    second_order_markov_chain = SecondOrderMarkovChain(word_list)

    print("Testing First Order Markov Chain")
    print(markov_chain.generate_sentence(10))
    print("\nTesting Second Order Markov Chain")
    print(second_order_markov_chain.generate_sentence(15))


if __name__ == "__main__":
    with open('voltaire-corpus/candide.txt', 'r') as corp_1, open('voltaire-corpus/the-works-of-voltaire-vol-iv.txt', 'r') as corp_2, open('voltaire-corpus/voltaires-philosophical-dictionary.txt', 'r') as corp_3:
        source_word_list = [word.lower() for word in corp_1.read().rsplit()]
        source_word_list.extend([word.lower() for word in corp_2.read().rsplit()])
        source_word_list.extend([word.lower() for word in corp_3.read().rsplit()])

    test_word_list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]


    test_markov_chain(source_word_list)
