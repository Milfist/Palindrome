from unittest import TestCase

from algorithm.palindrome import Palindrome


class PalindromeTest(TestCase):

    def test_should_be_return_true_when_check_is_palindrome(self):
        self.assertTrue(Palindrome.is_palindrome('reconocer'))

    def test_should_be_return_false_when_check_is_palindrome_wrong_word(self):
        self.assertFalse(Palindrome.is_palindrome('persona'))

    def test_should_be_return_false_when_check_is_palindrome_with_upper_case_and_space(self):
        self.assertFalse(Palindrome.is_palindrome('Se es o no se es'))

    def test_should_be_return_true_when_check_is_palindrome_with_transformed_text(self):
        self.assertTrue(Palindrome.is_palindrome(str.lower('Se es o no se es').replace(' ', '')))
