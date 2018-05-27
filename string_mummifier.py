class StringMummifier:
    VOWELS = 'aeiou'
    REPLACEMENT = 'mummy'

    def mummify(self, word):
        if self.__is_vowel_count_less_than_30_percent(word):
            return word
        return self.__replace_vowels(word)

    def __is_a_vowel(self, char):
        return char.lower() in StringMummifier.VOWELS

    def __is_vowel_count_less_than_30_percent(self, word):
        vowel_count = 0
        for char in word:
            if self.__is_a_vowel(char):
                vowel_count += 1
        return len(word) == 0 or vowel_count / len(word) < 0.3

    def __replace_vowels(self, word):
        mummified = ""
        for char in word:
            if not self.__is_a_vowel(char):
                mummified += char
            elif not mummified.endswith(StringMummifier.REPLACEMENT):
                mummified += StringMummifier.REPLACEMENT
        return mummified
