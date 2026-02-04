from collections import Counter
from functools import reduce
from itertools import chain
from typing import Iterable, Callable, Dict, Set, Generator, Any
import logging

def setup_logging(path: str = 'weather.log') -> None:
    logging.basicConfig(
        filename='main.log',
        filemode='w',
        level=logging.DEBUG,
        format='%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(funcName)s | %(message)s',
        encoding='utf-8'
    )

def _validate_texts(texts: Iterable[Any]) -> None:
    """Проверка входа: texts должен быть итерируемым (не строкой)."""
    if texts is None:
        raise TypeError("texts должен представлять собой итерируемый объект из строк, получен None")

    # Строка тоже iterable, но по смыслу нам нужен набор текстов, а не один текст
    if isinstance(texts, str):
        raise TypeError("texts должен представлять собой итерируемый объект строк (например, list[str]), а не одну строку.")

    try:
        iter(texts)
    except TypeError as e:
        raise TypeError("texts must be an iterable of strings") from e

def _validate_n(n):
    if not isinstance(n, int):
        raise TypeError("n должен быть int")
    if n < 0:
        raise ValueError("n должен быть >= 0")

def tokenize(texts: Iterable[Any]) -> Generator[str, None, None]:
    """
    Генератор: отдаёт слова по одному (часть = слово).
    Использует itertools.chain для "сплющивания" списков слов.
    """
    _validate_texts(texts)

    split_lists = [
        text.split()
        for text in texts
        if isinstance(text, str) and text.strip()
    ]

    # itertools.chain: превращаем list[list[str]] в поток слов
    for word in chain.from_iterable(split_lists):
        w = word.lower()
        if w.isalpha():
            yield w

def get_word_frequency(texts: Iterable[Any]) -> Dict[str, int]:
    """Словарь частотности слов по всем текстам."""
    return dict(Counter(tokenize(texts)))

def get_dict_state(
    func: Callable[[Iterable[str]], Dict[str, int]],
    texts: Iterable[Any]
) -> Dict[int, Dict[str, int]]:
    """
    Вложенный словарь статистики по каждому тексту.
    Ключ — индекс текста.
    """
    _validate_texts(texts)
    if not callable(func):
        raise TypeError("func должна быть callable")

    return {
        i: func([text])
        for i, text in enumerate(texts)
        if isinstance(text, str)
    }

def get_unique_words_by_length(texts: Iterable[Any], n: int) -> Set[str]:
    """Множество уникальных слов длиной > n."""
    _validate_n(n)
    return {word for word in tokenize(texts) if len(word) > n}

def get_generator_processing_text_parts(texts: Iterable[Any]) -> Generator[str, None, None]:
    """Генератор для обработки текста по частям (часть = слово)."""
    return tokenize(texts)

def merge_frequencies(*freq_dicts):
    """
    Пример functools: объединяем несколько частотных словарей в один.
    """
    for d in freq_dicts:
        if not isinstance(d, dict):
            raise TypeError("All arguments must be dict[str, int]")

    return reduce(lambda acc, d: acc + Counter(d), freq_dicts, Counter())

setup_logging()

texts = [
    "Привет мир",
    "Мир большой и красивый",
    "",
    None,
    "Python Python PYTHON!",
    "123 !!!",
]




logging.info('Тест: словарь частотности: {}'.format(get_word_frequency(texts)))
logging.info('Тест: вложенный словарь по каждому тексту: {}'.format(get_dict_state(get_word_frequency, texts)))
logging.info('Тест: множество уникальных слов длиннее 4: {}'.format(get_unique_words_by_length(texts, 4)))

gen = get_generator_processing_text_parts(texts)
logging.info('Тест: генератор обработки текста по частям')
logging.info(next(gen))
logging.info(next(gen))
logging.info(list(gen)) # Остальные списком

f1 = {'a': 2, 'b': 1}
f2 = {'a': 1, 'c': 3}
logging.info('Тест: functools (объединение словарей): {}'.format(merge_frequencies(f1, f2)))