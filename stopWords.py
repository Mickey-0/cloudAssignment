import nltk
from nltk.corpus import stopwords
from collections import Counter


nltk.download('stopwords')

def remove_stopwords(text):
    stopWords = set(stopwords.words('english'))
    words = text.split()
    return ' '.join([word for word in words if word.lower() not in stopWords])

def count_words(text):
    words = text.split()
    word_count = Counter(words)
    return word_count

def main():
    # read the file 
    with open('paragraphs.txt', 'r') as file:
        text = file.read()

    # remove stopword (زي a , an , and , but , or و هكذا)
    text_without_stopwords = remove_stopwords(text)

    # Count word
    word_count = count_words(text_without_stopwords)

    # Display words count
    print("Word count:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()