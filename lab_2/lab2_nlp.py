import gensim
import re

def run_model():
    # Задаем список позитивных слов
    words = ['столик_NOUN', 'кабинет_NOUN']

    model_file = "file_cbow.txt"
    # model_file = "D:\\file_cbow.txt"
    
    w2v_model = gensim.models.KeyedVectors.load_word2vec_format(model_file, binary=False)

    # Получаем векторы для 'столик_NOUN' и 'кабинет_NOUN'
    vector_table = w2v_model["столик_NOUN"]
    vector_office = w2v_model["кабинет_NOUN"]

    # Выполняем суммирование векторов
    total_vector = vector_table + vector_office

    # Ищем 10 ближайших слов к полученному вектору
    similar_words = w2v_model.most_similar(positive=[total_vector], topn=10)

    # Регулярное выражение для фильтрации слов с суффиксом "_NOUN"
    noun_pattern = re.compile("(.*)_NOUN")

    # Печатаем слова, которые соответствуют формату "_NOUN"
    for word in similar_words:
        match = noun_pattern.match(word[0])
        if match:
            print(match.group(1))

if __name__ == '__main__':
    run_model()
