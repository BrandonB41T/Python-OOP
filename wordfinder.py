"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dictionary_file = open(path)

        self.words = self.make_list(dictionary_file)

        print(f"{len(self.words)} words read")

    def make_list(self, dictionary_file):
        """Turn dictionary_file into a list."""

        return [w.strip() for w in dictionary_file]

    def random(self):
        """Return random word from list of words."""

        return random.choice(self.words)
    

class RevisedWordFinder(WordFinder):
    """Specialized word finder that doesn't acknowledge empty lines or comments

    >>> rwf = RevisedWordFinder("revised.txt")
    8 words read

    >>> rwf.random() not in ["money", "cars", "houses", "liquid", "gas", "solid", "hey", "hello"]
    False

    >>> rwf.random() not in ["money", "cars", "houses", "liquid", "gas", "solid", "hey", "hello"]
    False
    
    >>> rwf.random() not in ["money", "cars", "houses", "liquid", "gas", "solid", "hey", "hello"]
    False

    >>> rwf.random() not in ["money", "cars", "houses", "liquid", "gas", "solid", "hey", "hello"]
    False

    >>> rwf.random() not in ["money", "cars", "houses", "liquid", "gas", "solid", "hey", "hello"]
    False
    """
    def make_list(self, dictionary_file):
        """Turn dictionary_file into a list, ignoring blank lines and comments."""

        return [w.strip() for w in dictionary_file if not w.startswith("#") and w.strip()]
