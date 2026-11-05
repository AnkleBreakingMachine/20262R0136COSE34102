
def word_count(text):
    counts = {}

    for word in text.lower().split():
        word = word.strip(".,!?")
        counts[word] = counts.get(word, 0) + 1

    return counts

text = "Python is fun and Python is powerful"
print(word_count(text))