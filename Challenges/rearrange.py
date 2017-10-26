import sys
import random


def rearrange(words):
    rearranged_words = []

    while len(words) > 0:
        rearranged_words.append(words.pop(random.randint(0, len(words) - 1)))

    return rearranged_words


if __name__ == "__main__":
    params = sys.argv[1:]

    print(rearrange(params))

