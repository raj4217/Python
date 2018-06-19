def word_split(phrase, list_of_words, output=None):
    if not output:
        output = []
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            word_split(phrase[len(word):], list_of_words, output)
    return output
