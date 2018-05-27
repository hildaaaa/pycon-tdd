from unittest import TestCase

from string_mummifier import StringMummifier


class TestStringMummifier(TestCase):
    def test_should_not_mummify_empty_string(self):
        word = ""

        mummifier = StringMummifier()
        mummified_word = mummifier.mummify(word)

        self.assertEqual("", mummified_word)