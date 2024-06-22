"""
Word Occurrences
Estimate:   30 minutes
Actual:
"""

text = input("Enter a sentence: ").lower()
occurrences = {}
words = text.split()

for word in words:
    if word in occurrences:
        occurrences[word] += 1
    else:
        occurrences[word] = 1

for word in sorted(occurrences):
    print(f"{word} : {occurrences[word]}")