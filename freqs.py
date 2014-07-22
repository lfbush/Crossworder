import string

class LetterFrequency:
    def __init__(self):
        self.frequencies = {c: 0 for c in string.lowercase}

    def increment(self, letter):
        if letter in self.frequencies:
            self.frequencies[letter.toLowercase()] += 1

    def getCount(self, letter):
        return self.frequencies[letter]

    def getCounts(self):
        return self.frequencies

    def getTotalCount(self):
        return sum(self.frequencies.values())

    def getFrequency(self, letter):
        return self.getCount(letter) / self.getTotalCount()

    def getFrequencies(self):
        return {c: self.getFrequency(c) for c in self.frequencies.keys()}