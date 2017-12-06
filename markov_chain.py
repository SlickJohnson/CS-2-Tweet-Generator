"""Classes of different order Markov Chains."""
import random
from histograms import Dictogram


class FirstOrderMarkovChain(dict):
    """Implementation of a first order markov chain

    Attributes:
    """

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

def generate_sentence(length, model):
    """Return a sentence generated using a markov_chain."""
    current_word = random.choice(list(model))
    sentence = [current_word]

    for _ in range(0, length):
        current_dictogram = model[current_word]
        random_weighted_word = current_dictogram.get_weighted_random_word()
        current_word = random_weighted_word
        sentence.append(current_word)

    sentence[0] = sentence[0].capitalize()

    return ' '.join(sentence) + '.'


def test_markov_chain(word_list):
    """Test the functinality of markov chain."""
    histogram = Dictogram(word_list)
    print(histogram)

    markov_chain = FirstOrderMarkovChain(word_list)
    print(markov_chain)

    generated_sentence = generate_sentence(10, markov_chain)
    print(generated_sentence)


if __name__ == "__main__":
    SENTENCE = 'one fish two fish red fish blue fish'
    test_markov_chain(SENTENCE.split())
