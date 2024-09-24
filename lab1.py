# Импорт библиотек
import pymorphy3
import nltk

# Загрузка токенизатора NLTK
nltk.download('punkt_tab')


# Чтение файла
with open('file_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Токенизация текста
tokens = nltk.word_tokenize(text)

# Инициализация морфологического анализатора pymorphy3
morph = pymorphy3.MorphAnalyzer()

# Функция для проверки, является ли слово существительным или прилагательным
def is_noun_or_adj(word):
    parsed = morph.parse(word)[0]
    return parsed.tag.POS in ['NOUN', 'ADJF', 'ADJS']

# Функция для проверки совпадения граммем (род, число, падеж)
def match_grammemes(word1, word2):
    parsed1 = morph.parse(word1)[0]
    parsed2 = morph.parse(word2)[0]
    # Проверка рода, числа и падежа
    return (parsed1.tag.gender == parsed2.tag.gender and
            parsed1.tag.number == parsed2.tag.number and
            parsed1.tag.case == parsed2.tag.case)

# Извлечение соседних пар слов
valid_pairs = []

for i in range(len(tokens) - 1):
    word1, word2 = tokens[i], tokens[i+1]
    if is_noun_or_adj(word1) and is_noun_or_adj(word2) and match_grammemes(word1, word2):
        # Лемматизация слов
        lemma1 = morph.parse(word1)[0].normal_form
        lemma2 = morph.parse(word2)[0].normal_form
        valid_pairs.append((lemma1, lemma2))

print('\nFinal Result:\n')
# Вывод результатов
for pair in valid_pairs:
    print(pair)
