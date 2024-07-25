"""
Word Occurrences
Estimate:   30 minutes
Actual:     ~20 minutes (got distracted with B99, lost track of time)
"""

text = input("Enter a sentence: ").lower()
occurrences = {}
words = text.split()

for word in words:
    if word in occurrences:
        occurrences[word] += 1
    else:
        occurrences[word] = 1

max_width = max(len(word) for word in occurrences)

for word in sorted(occurrences):
    print(f"{word:{max_width}} : {occurrences[word]}")
