import re

_EXP = re.compile('\w+')


# returns dictionary that displays each unique word along with the number of times the word appears in the source text.
def get_histogram_dictionary(word_list):
    histogram = {}

    for word in word_list:
        if _EXP.match(word) is None:
            continue

        if word not in histogram:
            histogram.update({word: 0})

        histogram[word] += 1

    return histogram


# returns nested list that displays each unique word along with the number of times the word appears in the source text.
def get_histogram_list(word_list):
    histogram = []

    for word in word_list:
        if _EXP.match(word) is None:
            continue

        if not any(word in word_freq for word_freq in histogram):
            histogram.append((word, 0))

        histogram = [(w, f + 1) if w == word else (w, f) for w, f in histogram]

    return histogram


# returns nested list that displays each unique word along with the number of times the word appears in the source text.
def get_histogram_tuple(word_list):
    histogram = []

    for word in word_list:
        if _EXP.match(word) is None:
            continue

        if not any(word in word_freq for word_freq in histogram):
            histogram.append((word, 0))

        histogram = [[w, f + 1] if w == word else [w, f] for w, f in histogram]

    return histogram


# takes a histogram argument and returns the total count of unique words in the histogram
def unique_words(histogram):
    return len(histogram.keys())


# takes a word and histogram argument and returns the number of times that word appears in a text
def frequency(word, histogram):
    if word not in histogram:
        return 0

    return histogram[word]


def get_word_list():
    with open('holmes.txt', 'r', encoding= 'utf8') as source_file:
        source_word_list = [word.lower() for word in source_file.read().rsplit()]

    test_word_list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]

    return source_word_list


if __name__ == "__main__":
    word_list = get_word_list()
    source_histogram_dictionary = get_histogram_dictionary(word_list)
    # source_histogram_list = get_histogram_list(word_list)
    # source_histogram_tuple = get_histogram_tuple(word_list)

    print('Sorce histogram as a dictionary:\n\t', source_histogram_dictionary)
    # print('Sorce histogram as a list of lists:\n\t', source_histogram_list)
    # print('Sorce histogram as a list of tuples:\n\t', source_histogram_list)
