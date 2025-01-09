import unittest
from unittest import TestCase
from homeworks import (calculate_sums, multiplication_table, sum_numbers, arithmetic_mean, reverse_string,
                       longest_word, find_substring, count_unique_symbols, greater_10)

class TestCalculateSums(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_input = ['1, 2, 3', '4, 5', '6']
        cls.invalid_input = ["1, 2, a", "b, c"]
    def setUp(self):
        self.expected_valid = [6, 9, 6]
        self.expected_invalid = ["Не можу це зробити!", "Не можу це зробити!"]
    def test_valid_input(self):
        result = calculate_sums(self.valid_input)
        self.assertEqual(result, self.expected_valid)
    def test_invalid_input(self):
        result = calculate_sums(self.invalid_input)
        self.assertEqual(result, self.expected_invalid)

class TestMultiplicationTable(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.number = 5
    def setUp(self):
        self.expected_output = "5 x 1 = 5 5 x 2 = 10 5 x 3 = 15 5 x 4 = 20 5 x 5 = 25"
    def test_multiplication_table(self):
        result = multiplication_table(self.number)
        self.assertEqual(result, self.expected_output)

class TestSumNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        result = sum_numbers(3, 7)
        self.assertEqual(result, 10)

    def test_negative_numbers(self):
        result = sum_numbers(-4, -6)
        self.assertEqual(result, -10)

    def test_positive_and_negative(self):
        result = sum_numbers(5, -3)
        self.assertEqual(result, 2)

    def test_with_zero(self):
        result = sum_numbers(0, 8)
        self.assertEqual(result, 8)

class TestArithmeticMean(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.empty_list = []
        cls.single_value_list = [5]
        cls.multiple_values_list = [1, 2, 3, 4]
        cls.list_with_negative = [-2, -1, 0, 1, 2]

    def setUp(self):
        self.expected_empty = 0
        self.expected_single_value = 5
        self.expected_multiple_values = 2.5
        self.expected_with_negative = 0

    def test_empty_list(self):
        result = arithmetic_mean(self.empty_list)
        self.assertEqual(result, self.expected_empty)

    def test_single_value_list(self):
        result = arithmetic_mean(self.single_value_list)
        self.assertEqual(result, self.expected_single_value)

    def test_multiple_values_list(self):
        result = arithmetic_mean(self.multiple_values_list)
        self.assertEqual(result, self.expected_multiple_values)

    def test_list_with_negative(self):
        result = arithmetic_mean(self.list_with_negative)
        self.assertEqual(result, self.expected_with_negative)

class TestReverseString(unittest.TestCase):
    def test_empty_string(self):
        result = reverse_string("")
        self.assertEqual(result, "")

    def test_single_character(self):
        result = reverse_string("a")
        self.assertEqual(result, "a")

    def test_multiple_characters(self):
        result = reverse_string("hello")
        self.assertEqual(result, "olleh")

class TestLongestWord(unittest.TestCase):
    def test_empty_list(self):
        result = longest_word([])
        self.assertEqual(result, "")

    def test_single_word(self):
        result = longest_word(["hello"])
        self.assertEqual(result, "hello")

    def test_multiple_words(self):
        result = longest_word(["apple", "banana", "cherry"])
        self.assertEqual(result, "banana")

class TestFindSubstring(unittest.TestCase):
    def test_substring_present(self):
        result = find_substring("hello world", "world")
        self.assertEqual(result, 6)

    def test_substring_not_present(self):
        result = find_substring("hello world", "python")
        self.assertEqual(result, -1)

class TestCountUniqueSymbols(unittest.TestCase):
    def test_more_than_10_unique(self):
        result = count_unique_symbols("abcdefghijk")
        self.assertTrue(result)

    def test_exactly_10_unique(self):
        result = count_unique_symbols("abcdefghij")
        self.assertFalse(result)

    def test_less_than_10_unique(self):
        result = count_unique_symbols("aaaabbbbcc")
        self.assertFalse(result)

class TestGreater10(unittest.TestCase):

    def test_numbers_greater_than_10(self):
        numbers = [5, 12, 8, 15, 3]  # корректно создаем список
        result = greater_10(numbers)
        self.assertEqual(result, [12, 15])

    def test_no_numbers_greater_than_10(self):
        numbers = [5, 8, 3, 1]
        result = greater_10(numbers)
        self.assertEqual(result, [])

    def test_all_numbers_greater_than_10(self):
        numbers = [11, 12, 15, 100]
        result = greater_10(numbers)
        self.assertEqual(result, [11, 12, 15, 100])

if __name__ == "__main__":
    unittest.main()