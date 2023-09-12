import os
 
from basefilter import BaseFilter
from corpus import Corpus
from spam_words import SPAM_WORDS
 
PREDICTION_FILENAME = "!prediction.txt"
 
 
class MyFilter(BaseFilter):
 
    def __init__(self):
        self.spam_word_dict = {}
        self.spam_word_count = 0
 
    def decide(self, fname, body):
        self.count_to_dic(body.lower().split())
        self.spam_word_count = sum(self.spam_word_dict.values())
        if self.spam_word_count > 0:
            return "SPAM"
        else:
            return "OK"
 
    def count_to_dic(self, body):
        for word in SPAM_WORDS:
            self.spam_word_dict[word] = 0
 
        for i in range(len(body)):
            for j in range(1, len(SPAM_WORDS) + 1):
                phrase = ' '.join(body[i:i + j])
                if phrase in SPAM_WORDS:
                    self.spam_word_dict[phrase] += 1
 
 
if __name__ == '__main__':
    filter = MyFilter()
    fname = 0
 
    with open("./email", 'rt', encoding='utf-8') as f:
        body = f.read()
 
    print(filter.decide(fname, body))
