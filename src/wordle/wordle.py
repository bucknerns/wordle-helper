from __future__ import annotations
from itertools import chain
from collections import Counter
from typing import List

"""
This is a tool to help solve Wordle puzzles
"""


class Wordle:
    """A simple wordle helper"""

    original: List[str]
    """Lexicon to use for checking wordle matches"""

    lexicon: List[str]
    """Words that the object is considering, functions remove from this"""

    word_len: int
    """Length of words in the puzzle"""

    def __init__(self, path: str, export_lexicon: bool = False, word_len: int = 5) -> None:
        """Constructor

        Args:
            path: dir/filename of dictionary to be used
            export_lexicon: flag to see if worldle should export trimmed dictionary
            word_len: how long the words are in the puzzle
        """
        self.load_lexicon(path, export_lexicon, word_len)

    def load_lexicon(self, path: str, export_lexicon: bool = False, word_len: int = 5) -> None:
        """Loads lexicon from file and can save results if export_lexicon is set to True

        Args:
            path: dir/filename of dictionary to be used
            export_lexicon: flag to see if worldle should export trimmed dictionary
            word_len: how long the words are in the puzzle
        """
        self.word_len = word_len

        with open(path) as f:
            self.original = [x for x in f.read().splitlines() if len(x) == self.word_len]
            self.lexicon = self.original.copy()

        if export_lexicon:
            with open(path, 'w') as f:
                for word in self.lexicon:
                    f.write(f'{word}\n')

        print(f'Wordle has {len(self.original)} words available.')

    def reset(self) -> None:
        """If you are playing a new puzzle (or messed up the clues) use this to rest dict"""
        self.lexicon = self.original.copy()

    def doesnt_have(self, letters: List[str] | str = "") -> None:
        """Removes words that have the letter passed in

        Args:
            letters: a string, or array of strings to filter lexicon by
        """
        n_words = len(self.lexicon)
        self.lexicon = [x for x in self.lexicon if len(set(x)) == len(set(x) - set(letters))]
        print(f'{letters} have removed {n_words - len(self.lexicon)} words.')

    def has(self, letter: str, *, at: int = None, not_at: int = None) -> None:
        """Removes words that do not have the letter passed in

        Args:
            letter: string, character the word has
            at: int, which position the letter is (green)
            not_at: int, which position the letter is not at (yellow)
        """
        n_words = len(self.lexicon)
        if not_at is not None:
            self.lexicon = [x for x in self.lexicon if letter in x and x[not_at - 1] != letter]
        elif at is not None:
            self.lexicon = [x for x in self.lexicon if x[at - 1] == letter]
        else:
            self.lexicon = [x for x in self.lexicon if letter in x]

        print(f'{letter} has removed {n_words - len(self.lexicon)} words.')

    def whats_left(self) -> None:
        """Print all possible remaining words"""
        print(self.lexicon)

    def term_frequency(self) -> None:
        """Calculates the term frequency to suggest words to use for guessing

        This function gets the current lexicon's term frequency and then displays the most
        'valuable' words based on non-repeating high tf. This helps elimates words from
        the lexicon e.g. if you guess 'fuzzy' and wordle tells you the 'z' is nowhere in
        the word, that isn't very helpful, however if a letter with a high tf is nowhere
        in the word then you can elimate a large number of possibilites.
        """

        letter_count = len(self.lexicon) * self.word_len
        # count each term and convert it to a tf
        letter_weights = {k: v / letter_count for k, v in Counter(chain(*self.lexicon)).items()}

        # calculate how "valuable" each word is in terms of the frequency of letters it contains
        # this should help us narrow down letters e.g. 'arose' has more common letters than 'kudzu'
        word_weights = {x: 0.0 for x in self.lexicon}
        for word in self.lexicon:
            value = 0
            # set is an easy way to remove duplicates, if we don't remove these then words with
            # repeating high value letters will seem more valuable e.g. reese
            for letter in set(word):
                value += letter_weights[letter]
            word_weights[word] = value
        print(sorted(word_weights, key=lambda x: word_weights[x])[-5:])

    def enter_word(self, word: str, *results: int):
        if not (len(results) == len(word) == self.word_len):
            print(f"Enter must enter word and results of length {self.word_len}")
            return
        for index, (letter, result) in enumerate(zip(word, results), 1):
            if result in {0, None, "0"}:
                self.doesnt_have(letter)
            elif result in {False, -1, "-"}:
                self.has(letter, not_at=index)
            elif result in {1, True, "1"}:
                self.has(letter, at=index)
