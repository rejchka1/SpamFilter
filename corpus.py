import os
 
 
class Corpus:
    def __init__(self, email_directory):
        self.email_directory = email_directory
 
    def emails(self):
        email_names = os.listdir(self.email_directory)
 
        for fname in email_names:
            if fname[0] == '!':
                pass
            else:
                with open(self.email_directory + "/" + fname, "rt", encoding="utf-8") as f:
                    yield(fname, f.read())
