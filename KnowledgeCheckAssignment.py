#1 Even or Odd
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

print(even_or_odd(22))
print(even_or_odd(19))

#2 Convert a number into a String
def number_to_string(num):
    return str(num)

print(number_to_string(24))
print(number_to_string(-23))

#3 Vowel Count
def get_count(sentence):
    vowels = "aeiou"
    return sum(1 for char in sentence if char in vowels)

print(get_count("hello world"))