import string
from collections import Counter
def count_word_frequencies(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    word_freq = Counter(words)
    return word_freq
text = input("please enter the text")
word_frequencies = count_word_frequencies(text)
for word, frequency in word_frequencies.items():
    print(f"{word}: {frequency}")
