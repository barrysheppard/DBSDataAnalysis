# This is the code we used as we worked our way through the problem.

# Based on the tutorial below – and we’ll see where we end up in class
# http://www.openbookproject.net/py4fun/spellCheck/


class SpellChecker(object):
    ''' Used to check spelling '''

    def __init__(self):
        self.words = []

    def load_file(self, file_name):
        my_file = open(file_name)
        lines = my_file.readlines()
        my_file.close()
        return list(map(lambda x: x.strip(), lines))

    # create a function to load the words and to check a word is in the
    # dictionary
    def load_words(self, file_name):
        ''' loads up a file of words and returns it as a list'''
        self.words = self.load_file(file_name)

    # This was the original check which just checked one word
    def check_word(self, word):
        ''' This checks if the word is in the list words'''
        return word.lower().strip('.') in self.words

    # We expand this out into a sentence rather than a single word
    def check_words(self, sentence):
        words_to_check = sentence.split(' ')
        failed_words = []
        for word in words_to_check:
            if not self.check_word(word):
                print('Word is misspelt : ' + word)
                failed_words.append(word)
        return failed_words

    # To expand this to checking a document
    def check_document(self, file_name):
        ''' accepts a file name, returns list of incorrect spellings'''
        self.sentences = self.load_file(file_name)
        failed_words_in_sentences = []
        for index, sentence in enumerate(self.sentences):
            failed_words_in_sentences.extend(self.check_words(sentence))
        return failed_words_in_sentences


# enable so that this is only called when the script run from the command line
if __name__ == '__main__':
    # This is the path name for our dictionary file
    fname = '/Users/barrysheppard/Github/DBSDataAnalysis/BigData/04Lecture/'
    fname = fname + 'spell.words'

    dictionary = SpellChecker()
    dictionary.load_words(fname)

    # Here we are checking a single word
    # print(dictionary.check_words('zygotic mistasdas elementary asdfasdf'))
    # print(len(dictionary.check_words('zygotic')))

    # Lets try a different document
    fname = '/Users/barrysheppard/Github/DBSDataAnalysis/BigData/04Lecture/'
    fname = fname + 'test.txt'
    dictionary.check_document(fname)
