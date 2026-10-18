# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

import random
from faker import Faker
fake = Faker()

# Random sentence
sen = fake.sentence()
#print(sen)

# Random paragraph
para = fake.paragraph()
#print(para)


# Your custom keywords
keywords = ["automation", "python", "selenium", "testing", "API", 'buy now', 'subscribe this']

def random_sentence(keywords, word_count=8):
    words = [random.choice(keywords) for _ in range(word_count)]
    sentence = " ".join(words).capitalize() + "."
    return sentence

def random_paragraph(keywords, sentence_count=2):
    return " ".join(random_sentence(keywords, random.randint(6, 10)) for _ in range(sentence_count))

# Generate 3 paragraphs
for i in range(3):
    print(f"Paragraph {i+1}:\n{random_paragraph(keywords)}\n")

para1 = random_paragraph(keywords, sentence_count=5)
print(para1)

spam_words = ['Make a lot of money', 'buy now', 'subscribe this', 'click this']
print(spam_words)

for i in range(len(spam_words)-1):
    if spam_words[i] in para1:
        print('This is spam')
    else:
        print('content looks good')