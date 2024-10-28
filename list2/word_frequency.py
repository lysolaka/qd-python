import string
import matplotlib.pyplot as plt


with open("word_frequency.txt", "r") as file:
    text = str(file.read())

words = (text
         .lower()
         .translate(str.maketrans("", "", string.punctuation))
         .split())

word_count = {}
for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1

plt.bar(list(word_count.keys()), list(word_count.values()))
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.title("Word Frequency")
plt.show()
