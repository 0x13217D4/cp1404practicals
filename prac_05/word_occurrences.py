word_to_count = {}
maximum_length = 0
text = input("Text: ")
words = text.split()

for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
    if len(word) > maximum_length:
        maximum_length = len(word)

for word in sorted(word_to_count):
    print(f"{word:{maximum_length}} : {word_to_count[word]}")