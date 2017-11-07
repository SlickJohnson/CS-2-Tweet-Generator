import histogram as hist
import random
import secrets


def get_weighted_sample(histogram):
    items = histogram.items()
    total = sum(freq for word, freq in items)
    random_num = secrets.randbelow(total)

    weight = 0
    for word, freq in items:
        if weight + freq >= random_num:
            return word

        weight += freq


def get_random_sentence(file_path):
    with open(file_path, 'r', encoding='utf8') as source_file:
        source_word_list = [word.lower() for word in source_file.read().rsplit()]

    histogram = hist.get_histogram_dictionary(source_word_list)

    return " ".join([get_weighted_sample(histogram) for _ in range(random.randint(5, 15))])


if __name__ == "__main__":
    # sentence = "one fish two fish red fish blue fish"
    # word_list = sentence.split()  # sys.argv[1:]
    # histogram = hist.get_histogram_dictionary(word_list)
    #
    # samples_list = [get_weighted_sample(histogram.items()) for i in range(1000000)]
    #
    # samples_histogram = hist.get_histogram_dictionary(samples_list)

    print(get_random_sentence('holmes.txt'))
