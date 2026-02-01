from collections import Counter

def get_word_frequency(texts):

    words = (
        word.lower()
        for text in texts
        for word in text.split()
        if word.isalpha()
    )

    return dict(Counter(words))

