import unittest

from spellcheck import SpellChecker


class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.spellChecker = SpellChecker()
        # This is the path name for our dictionary file
        file_name = '/Users/barrysheppard/Github/DBSDataAnalysis/'
        file_name = file_name + 'BigData/04Lecture/spell.words'
        self.spellChecker.load_words(file_name)

    def test_spell_checker(self):
        self.assertTrue(self.spellChecker.check_word('zygotic'))
        failed_words = self.spellChecker.check_words('zygotic mistasdas elementary')
        self.assertEqual(1, len(failed_words))
        self.assertEqual('mistasdas', failed_words[0]['word'])
        self.assertEqual(1, failed_words[0]['line'])
        self.assertEqual(9, failed_words[0]['pos'])
        self.assertEqual(0, len(self.spellChecker.check_words('our first correct sentence')))
        # handle case sensitivity
        self.assertEqual(0, len(self.spellChecker.check_words('Our capital sentence')))
        # handle full stop
        self.assertEqual(0, len(self.spellChecker.check_words('Our full stop sentence.')))
        failed_words = self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary')
        self.assertEqual(2, len(failed_words))
        self.assertEqual('mistasdas', failed_words[0]['word'])
        self.assertEqual(1, failed_words[0]['line'])
        self.assertEqual(9, failed_words[0]['pos'])
        self.assertEqual('spelllleeeing', failed_words[1]['word'])
        self.assertEqual(1, failed_words[1]['line'])
        self.assertEqual(19, failed_words[1]['pos'])
        self.assertEqual(0, len(self.spellChecker.check_document('spell.words')))

if __name__ == '__main__':
    unittest.main()
