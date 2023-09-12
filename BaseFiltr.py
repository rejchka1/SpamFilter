import os
from corpus import Corpus
 
PREDICTION_FILENAME = "!prediction.txt"
 
 
class BaseFilter:
    def train(self, test_corpus_dir):
        pass
 
    def test(self, test_corpus_dir):
        corpus = Corpus(test_corpus_dir)
        pred_class = {}
        for fname, body in corpus.emails():
            pred_class[fname] = self.decide(fname, body)
 
        predfpath = os.path.join(corpus.email_directory, PREDICTION_FILENAME)
        with open(predfpath, 'wt', encoding='utf-8') as f:
            for name, cls in pred_class.items():
                f.write(name + ' ' + cls + '\n')
 
    def decide(self, fname, body):
        raise NotImplementedError("Child filter has to implement 'decide' method!")
