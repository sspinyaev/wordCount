import re

class WordCounter:
    def __init__(self):
        self.word_counts = {}

    def load(self, filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
                words = re.findall(r'\b[a-zA-Z]+\b', content)
                for word in words:
                    self.word_counts[word] = self.word_counts.get(word, 0) + 1
                print(f"Слова загружены из '{filename}'")
        except FileNotFoundError:
            print(f"File '{filename}' not found")

    def wordcount(self, word):
        count = self.word_counts.get(word, 0)
        print(f"Насчитали слово '{word}' {count} times")

    def clear_memory(self):
        self.word_counts.clear()
        print("Память снова почищена")

def main():
    word_counter = WordCounter()

    while True:
        command = input("Ввести команду ")
        parts = command.split()

        if parts[0] == "load" and len(parts) == 2:
            word_counter.load(parts[1])
        elif parts[0] == "wordcount" and len(parts) == 2:
            word_counter.wordcount(parts[1])
        elif parts[0] == "clear-memory":
            word_counter.clear_memory()
        else:
            print("Ошибочка")

if __name__ == "__main__":
    main()