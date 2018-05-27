from unittest import TestCase

from string_mummifier import StringMummifier


class StringMummifierTestCase(TestCase):

    def test_should_not_mummify_empty_string(self):
        self.assert_correct_mummification("", "")

    def test_should_not_mummify_words_with_no_vowels(self):
        self.assert_correct_mummification("str", "str")

    def test_should_mummify_a_vowel(self):
        self.assert_correct_mummification("mummy", "a")

    def test_should_mummify_consonents_and_a_vowel(self):
        self.assert_correct_mummification("blmummy", "bla")

    def test_should_not_mummify_less_than_30_percent_vowels(self):
        self.assert_correct_mummification("blah", "blah")

    def test_should_mummify_continuous_vowels_once(self):
        self.assert_correct_mummification("hmummyr", "hear")

    def test_should_mummify_multiple_sets_of_vowels(self):
        self.assert_correct_mummification("blmummyhmummyh", "blaahah")

    def test_should_mummify_capital_vowels(self):
        self.assert_correct_mummification("blmummyhmummy", "blAhE")

    def test_should_error_on_none_input(self):
        with self.assertRaises(Exception):
            StringMummifier().mummify(None)

    def assert_correct_mummification(self, expected, word):
        mummifier = StringMummifier()
        mummified_word = mummifier.mummify(word)
        self.assertEqual(expected, mummified_word)

