"""Functions related to markov chains."""
from histograms import Dictogram
import random


def make_markov_chain(data):
    """Return a markov chain."""
    markov_model = dict()

    for i in range(0, len(data) - 1):
        if data[i] in markov_model:
            markov_model[data[i]].update([data[i + 1]])
        else:
            markov_model[data[i]] = Dictogram([data[i + 1]])

    return markov_model


def generate_sentence(length, model):
    """Return a sentence generated using a markov_chain."""
    current_word = random.choice(list(model))
    sentence = [current_word]

    for i in range(0, length):
        current_dictogram = model[current_word]
        random_weighted_word = current_dictogram.get_weighted_random_word()
        current_word = random_weighted_word
        sentence.append(current_word)

    sentence[0] = sentence[0].capitalize()

    return ' '.join(sentence) + '.'
    return sentence


def test_markov_chain(word_list):
    """Test the functinality of markov chain."""
    histogram = Dictogram(word_list)
    print(histogram)

    model = make_markov_chain(word_list)
    print(model)

    generated_sentence = generate_sentence(10, model)
    print(generated_sentence)


if __name__ == "__main__":
    sentence = 'one fish two fish red fish blue fish'
    word_list = sentence.split()

    test_markov_chain(word_list)
