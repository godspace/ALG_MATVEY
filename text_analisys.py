import string
import re

class TextAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'r') as file:
            text = file.read()
            self.text = self.clean_text(text)
        self.word_counts = {}

    def clean_text(self, text):
        """Cleans the text by removing punctuation and converting to lowercase."""
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text

    def words_counter(self):
        """Analyzes the text and returns a dictionary of word frequencies."""
        words = self.text.split()
        for word in words:
            if word in self.word_counts:
                self.word_counts[word] += 1
            else:
                self.word_counts[word] = 1
        return self.word_counts

    def most_common_words(self):
        """Sorts word counts by frequency and returns top 10 most common words."""
        sorted_words = sorted(self.word_counts.items(), key=lambda x: x[1], reverse=True)
        common_words = []
        for word, count in sorted_words:
            if len(word) > 3:
                common_words.append((word, count))
            if len(common_words) == 10:
                break
        return common_words

    def find_names(self):
        common_names = ["мария", "анна", "соня", "николай", "иван", "пьер", "элен", "андрей", 
                        "наташа", "миша", "денис", "долохов", "багратион", "бессонов", 
                        "болконский", "безухов", "ростов", "шерер", "дроздов", "курагин", 
                        "межов", "ахросимова", "кутузов", "давыдов", "храповицкий", "балага", 
                        "шиншин", "гелих", "ржевский", "бонапарт"]
        names_count = {}
        words = re.findall(r'\b\w+\b', self.text.lower())
        for word in words:
            if word in common_names:
                if word in names_count:
                    names_count[word] += 1
                else:
                    names_count[word] = 1
        sorted_names = sorted(names_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_names

filename = "Толстой Лев. Война и мир. Книга 1 - royallib.ru.txt"
analyzer = TextAnalyzer(filename)
word_counts = analyzer.words_counter()

most_common_words = analyzer.most_common_words()

names = analyzer.find_names()
print(names)