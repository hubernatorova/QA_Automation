import lst


def calculate_sums(strings):
    results = []
    for string in strings:
        try:
            numbers = list(map(int, string.split(',')))
            total = sum(numbers)
            results.append(total)
        except ValueError:
            results.append("Не можу це зробити!")
    return results

def multiplication_table(number):
    final = []
    multiplier = 1
    while True:
        result = number * multiplier
        if result > 25:
            break
        output = f"{number} x {multiplier} = {result}"
        final.append(output)
        multiplier += 1
    return " ".join(final)

def sum_numbers(a, b):
    return a + b

def arithmetic_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def reverse_string(s):
    return s[::-1]

def longest_word(words):
    if not words:
        return ""
    return max(words, key=len)

def find_substring(str1, str2):
    return str1.find(str2)

def count_unique_symbols(string_text):
    unique_symbols = len(set(string_text))
    if unique_symbols > 10:
        return True
    else:
        return False

def criteria(i):
    if i > 10:
        return i
def greater_10(numbers):
    resultus = list(filter(criteria,numbers))
    return resultus
