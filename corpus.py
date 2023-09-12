import email
import os
 
 
class Corpus:
    def __init__(self, email_directory):
        self.email_directory = email_directory
 
    def emails(self):
        email_names = os.listdir(self.email_directory)
        for name in email_names:
            file = self.email_directory+'/'+name
            if not name[0] == '!':
                with open(file, 'rt', encoding='utf-8') as f:
                    yield [name, f.read()]
 
        return email_names
 
 
if __name__ == '__main__':
    corpus = Corpus("./1")
    print(corpus.emails())
