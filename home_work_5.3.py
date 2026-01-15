
#ДЗ 5.3. hashtag 

import string

text = input("Enter your text: ")

for ch in string.punctuation:
    text = text.replace(ch, "")

words = text.split()
hashtag = "#" + "".join(word.capitalize() for word in words)
hashtag = hashtag[:140]

print(hashtag)
