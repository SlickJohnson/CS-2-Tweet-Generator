import random
import sys
import time

from rearrange import rearrange


def get_words_from_file(words_file, number_of_words_to_get=None):
    lines_from_file = words_file.read().splitlines()
    n = number_of_words_to_get if number_of_words_to_get is not None else len(lines_from_file)
    words_to_rearrange = random.sample(lines_from_file, n)

    return ' '.join(rearrange(words_to_rearrange))


if __name__ == "__main__":
    file = open("/usr/share/dict/words", "r")
    n = int(sys.argv[1]) if len(sys.argv) > 1 else None
    start = time.time()
    print(get_words_from_file(file, n))
    end = time.time()
    print("\n\t\tTook", end - start, "to run code")