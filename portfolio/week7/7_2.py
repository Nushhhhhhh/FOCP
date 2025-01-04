# Write and test three functions that each take two words (strings) as parameters and return sorted lists (as defined above) representing respectively:
# Letters that appear in at least one of the two words. Letters that appear in both words. Letters that appear in either word, but not in both

# function that return letters that appear in at least one of the two words
def either_word(word1, word2):
    union= set(word1) | set(word2)
    return sorted(union)
# function that return letters that appear in both words
def both_words(word1, word2):
    intesection= set(word1) & set(word2)
    return sorted(intesection)
# function that return letters that appear in eaither word, but not both
def one_word_only(word1, word2):
    symmetric_difference= set(word1) ^ set(word2)
    return sorted(symmetric_difference)
# input two strings from the user
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
# displaying the result
print(f"Letters that appear in at least one of the two words: {either_word(word1, word2)}")
print(f"Letters that appear in both words: {both_words(word1, word2)}")
print(f"Letters that appear in either word, but not in both: {one_word_only(word1, word2)}")