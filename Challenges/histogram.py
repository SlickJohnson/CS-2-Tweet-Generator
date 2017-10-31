import re


# returns data that displays each unique word along with the number of times the word appears in the source text.
def histogram(word_list):
    exp = re.compile('\w+')
    histogram = {}

    for word in word_list:
        if exp.match(word) is None:
            continue

        if word not in histogram:
            histogram.update({word: 0})

        histogram[word] += 1

    return histogram


# takes a histogram argument and returns the total count of unique words in the histogram
def unique_words(histogram):
    return len(histogram.keys())


# takes a word and histogram argument and returns the number of times that word appears in a text
def frequency(word, histogram):
    if word not in histogram:
        return 0

    return histogram[word]


if __name__ == "__main__":
    source_file = open('holmes.txt')
    source_word_list = [word.lower() for word in source_file.read().rsplit()]
    source_histogram = histogram(source_word_list)

    print('Source histogram:\t', source_histogram, '\n\n')
    print('Number of unique words:\t', unique_words(source_histogram), '\n\n')
    print('Frequency of word "holmes":\t', frequency('holmes', source_histogram), '\n\n')
