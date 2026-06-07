import random
import sys

import pykakasi
import regex
import wordfreq


def is_hiragana(text: str) -> bool:
    return regex.fullmatch(r"\p{Hiragana}+", text) is not None


def main():
    if len(sys.argv) == 1:
        word_length = 6

    else:
        word_length = int(sys.argv[1])

    kakasi = pykakasi.kakasi()

    word_set = set()

    for ja_word in wordfreq.top_n_list(lang="ja", n=100000):
        if not is_hiragana(ja_word):
            continue

        word = "".join(x["hepburn"] for x in kakasi.convert(ja_word))

        if len(word) != word_length:
            continue

        word_set.add(word)

    print(f"{len(word_set)} words found", file=sys.stderr)

    print(random.choice(sorted(word_set)))


if __name__ == "__main__":
    main()
