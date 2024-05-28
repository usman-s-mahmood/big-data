from collections import Counter
import re

def calculate_word_frequency(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())
        word_freq = Counter(words)
    return word_freq

def display_top_words(word_freq, top_n):
    top_words = word_freq.most_common(top_n)
    print(f"Top {top_n} most frequent words:")
    for word, frequency in top_words:
        print(f"{word}: {frequency}")

def main():
    file_path = input("Enter the path of the text file or enter 1 for default file: ")
    if file_path == '1':
        file_path = 'task4TXT.txt'
    top_n = int(input("Enter the number of top words to display: "))
    try:
        word_freq = calculate_word_frequency(file_path)
        display_top_words(word_freq, top_n)
    except Exception as error:
        print(f'Invalid filename!')
if __name__ == "__main__":
    main()

