# Q4: Word Frequency Counter

text = input("Enter a sentence: ")

words = text.lower().split()

word_count = {}

for word in words:
    word = word.strip(".,!?;:")

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nWord Frequency:")
for word, count in word_count.items():
    print(word, ":", count)

if word_count:
    most_common = max(word_count, key=word_count.get)
    print("\nMost frequent word:", most_common)
    print("Frequency:", word_count[most_common])
else:
    print("No words found.")