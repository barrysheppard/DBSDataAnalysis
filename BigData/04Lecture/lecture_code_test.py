
import unittest
from lecture_code import SpellChecker


class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.spellChecker = SpellChecker()
        file_name = '/Users/barrysheppard/Github/DBSDataAnalysis/'
        file_name = file_name + 'BigData/04Lecture/spell.words'
        self.spellChecker.load_words(file_name)

    def test_spell_checker(self):
        self.assertTrue(self.spellChecker.check_word('zygotic'))
        sentence = 'zygotic mistasdas elementary'
        result = ['mistasdas']
        self.assertEqual(result, self.spellChecker.check_words(sentence))
        sentence = 'our first correct sentence'
        result = []
        self.assertEqual(result, self.spellChecker.check_words(sentence))
        # # handle case sensitivity
        sentence = 'Our first correct Sentence'
        result = []
        self.assertEqual(result, self.spellChecker.check_words(sentence))
        # # handle full stop
        sentence = 'Our first correct Sentence'
        result = []
        self.assertEqual(result, self.spellChecker.check_words(sentence))
        sentence = 'zygotic mistasdas spelllleeeing elementary'
        result = ['mistasdas', 'spelllleeeing']
        self.assertEqual(result, self.spellChecker.check_words(sentence))


if __name__ == '__main__':
    unittest.main()
