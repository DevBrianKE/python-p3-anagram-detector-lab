# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        sorted_original = sorted(self.word.lower())
        result = []

        for w in word_list:
            if sorted(w.lower()) == sorted_original and w.lower() != self.word.lower():
                result.append(w)
        return result
