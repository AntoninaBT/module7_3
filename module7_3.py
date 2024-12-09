# Teplova //

from pprint import pprint
class WordsFinder:
    def __init__(self, *file_names):  # неограниченного количество названий файлов
        self.file_names = file_names

    def get_all_words(self):
        # пустой словарь all_words.
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                for symbol in [',', '.', '=', '!', '?', ';', ':']:
                    content = content.replace(symbol, '')
                content = content.replace(' - ', ' ')  # Обрабатываем пробелы вокруг тире
                words = content.split()  # Разделяем строки на слова
                all_words[file_name] = words
        return all_words

    def find(self, word):
        """
        Возвращает словарь: ключ - имя файла, значение - позиция первого вхождения слова.
        Если слово не найдено, файл не включается в результат.
        """

        positions = {}
        for file_name, words in self.get_all_words().items():
            try:
            # Слово ищем в нижнем регистре, возвращаем позицию +1 (счёт начинается с 1)
                positions[file_name] = words.index(word.lower()) + 1
            except ValueError:
            # Если слово не найдено, пропускаем
                continue
        return positions

    def count(self, word):
    # Возвращает словарь: ключ - имя файла, значение - количество вхождений слова.
        counts = {}
        for file_name, words in self.get_all_words().items():
        # Подсчитываем количество слова в нижнем регистре
            counts[file_name] = words.count(word.lower())
        return counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
