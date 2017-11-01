import histogram as hist
from itertools import chain
import sys
import secrets


def get_weighted_sample(histogram):
    total = sum(freq for word, freq in histogram)
    random_num = secrets.randbelow(total)

    weight = 0
    for word, freq in histogram:
        if weight + freq >= random_num:
            return word

        weight += freq


if __name__ == "__main__":
    sentence = "one fish two fish red fish blue fish"
    word_list = sentence.split()  # sys.argv[1:]
    histogram = hist.get_histogram_dictionary(word_list)

    samples_list = [get_weighted_sample(histogram.items()) for i in range(1000000)]

    samples_histogram = hist.get_histogram_dictionary(samples_list)
    print(samples_histogram)
