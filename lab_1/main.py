"""
Lab 1
A concordance extraction
"""


import re


def tokenize(text: str) -> list:
    """
    Splits sentences into tokens, converts the tokens into lowercase, removes punctuation
    :param text: the initial text
    :return: a list of lowercased tokens without punctuation
    e.g. text = 'The weather is sunny, the man is happy.'
    --> ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy']
    """
    if not isinstance(text, str):
        return []
    text_output = re.sub('[^a-z \n]', '', text.lower()).split()
    return text_output

    if not isinstance(text, str):
        return []

    text = text.lower()
    text = text.replace('\n', ' ')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    new_text = ''
    for symbol in text:
        if symbol in letters or symbol == ' ':
            new_text += symbol
    return new_text.split()

def remove_stop_words(tokens: list, stop_words: list) -> list:
    """
    Removes stop words
    :param tokens: a list of tokens
    :param stop_words: a list of stop words
    :return: a list of tokens without stop words
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy']
    stop_words = ['the', 'is']
    --> ['weather', 'sunny', 'man', 'happy']
    """
    if not isinstance(tokens, list):
        return []
    list_words = [word for word in tokens if word not in stop_words]
    return list_words

    if not isinstance(tokens, list):
        return []
    if not isinstance(stop_words, list):
        return tokens

    for word in stop_words:
        while word in tokens:
            tokens.remove(word)
    return tokens


def calculate_frequencies(tokens: list) -> dict:
    """
    Calculates frequencies of given tokens
    :param tokens: a list of tokens without stop words
    :return: a dictionary with frequencies
    e.g. tokens = ['weather', 'sunny', 'man', 'happy']
    --> {'weather': 1, 'sunny': 1, 'man': 1, 'happy': 1}
    """
    if not isinstance(tokens, list):
        return {}
    if len(tokens) > 0 and not isinstance(tokens[0], str):
        return {}
    set_words = set(tokens.copy())
    dict_freq = {word: tokens.count(word) for word in set_words}
    return dict_freq

    if not isinstance(tokens, list):
        return {}

    freq_dict = {}
    for token in tokens:
        if isinstance(token, str):
            frequency = tokens.count(token)
            freq_dict[token] = frequency
    return freq_dict


def get_top_n_words(freq_dict: dict, top_n: int) -> list:
    """
    Returns the most common words
    :param freq_dict: a dictionary with frequencies
    :param top_n: a number of the most common words to return
    :return: a list of the most common words
    e.g. tokens = ['weather', 'sunny', 'man', 'happy', 'and', 'dog', 'happy']
    top_n = 1
    --> ['happy']
    """
    if not isinstance(freq_dict, dict) or not isinstance(top_n, int):
        return []
    list_output = sorted(freq_dict, key=freq_dict.get, reverse=True)
    return list_output[:top_n]

    if not isinstance(freq_dict, dict) or not isinstance(top_n, int):
        return []

    # the number of words (from the most popular)
    values_of_words = []
    for value in freq_dict.values():
        if value in values_of_words:
            continue
        values_of_words.append(value)
    values_of_words.sort()
    values_of_words = values_of_words[::-1]
    # top_values
    top = values_of_words[:top_n]
    #
    top_words = []  # can be words with the same frequency
    for element in top:
        for word, frequency in freq_dict.items():
            if element == frequency:
                top_words.append(word)
    return top_words[:top_n]


def get_concordance(tokens: list, word: str, left_context_size: int, right_context_size: int) -> list:
    """
    Gets a concordance of a word
    A concordance is a listing of each occurrence of a word in a text,
    presented with the words surrounding it
    :param tokens: a list of tokens
    :param word: a word-base for a concordance
    :param left_context_size: the number of words in the left context
    :param right_context_size: the number of words in the right context
    :return: a concordance
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy',
                    'the', 'dog', 'is', 'happy', 'but', 'the', 'cat', 'is', 'sad']
    word = 'happy'
    left_context_size = 2
    right_context_size = 3
    --> [['man', 'is', 'happy', 'the', 'dog', 'is'], ['dog', 'is', 'happy', 'but', 'the', 'cat']]
    """
    stop = False
    if not isinstance(tokens, list) or not isinstance(word, str) or len(word) == 0:
        return []
    if not isinstance(left_context_size, int) or isinstance(left_context_size, bool):
        stop = True
    if not isinstance(right_context_size, int) or isinstance(right_context_size, bool):
        stop = True
    if len(tokens) > 0 and not isinstance(tokens[0], str):
        stop = True
    if stop:
        return []

    list_all_words = tokens.copy()
    indexes = [ind for ind, char in enumerate(list_all_words) if char == word]

    if len(indexes) == 0 or right_context_size < 0 or left_context_size < 0:
        return []
    if right_context_size == 0 and left_context_size == 0:
        return []
    if (indexes[-1] + right_context_size) > len(tokens):
        right_context_size = len(tokens)

    if (indexes[0] - left_context_size) < 0:
        list_output = [tokens[0:ind + 1 + right_context_size] for ind in indexes]
    else:
        list_output = [tokens[ind - left_context_size:ind + 1 + right_context_size] for ind in indexes]
    return list_output

    check_tokens = isinstance(tokens, list)
    check_word = isinstance(word, str)
    check_left_context_size = isinstance(left_context_size, int)
    check_right_context_size = isinstance(right_context_size, int)

    if not check_tokens or not check_word:
        return []
    if (not check_left_context_size and not check_right_context_size) or (left_context_size < 1 \
            and right_context_size < 1):
        return []
    if isinstance(left_context_size, bool) or isinstance(right_context_size, bool):
        return []

    if left_context_size < 1:
        left_context_size = 0
    elif right_context_size < 1:
        right_context_size = 0

    concordance = []
    for index, token in enumerate(tokens):
        if token == word:
            mini_concordance = tokens[index - left_context_size: index + right_context_size + 1]
            concordance.append(mini_concordance)
    return concordance


def get_adjacent_words(tokens: list, word: str, left_n: int, right_n: int) -> list:
    """
    Gets adjacent words from the left and right context
    :param tokens: a list of tokens
    :param word: a word-base for the search
    :param left_n: the distance between a word and an adjacent one in the left context
    :param right_n: the distance between a word and an adjacent one in the right context
    :return: a list of adjacent words
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy',
                    'the', 'dog', 'is', 'happy', 'but', 'the', 'cat', 'is', 'sad']
    word = 'happy'
    left_n = 2
    right_n = 3
    --> [['man', 'is'], ['dog, 'cat']]
    """
    concordance = get_concordance(tokens, word, left_n, right_n)
    if len(concordance) == 0:
        return []

    if left_n == 0:
        output = [[concord[-1]] for concord in concordance]
    elif right_n == 0:
        output = [[concord[0]] for concord in concordance]
    else:
        output = [[context[0], context[-1]] for context in concordance]
    return output


def read_from_file(path_to_file: str) -> str:
    """
    Opens the file and reads its content
    :return: the initial text in string format
    """
    with open(path_to_file, 'r', encoding='utf-8') as file_to_read:
        data = file_to_read.read()

    return data


def write_to_file(content: list, path_to_file='report.txt'):
    """
    Writes the result in a file
    """
    list_strings = [' '.join(concordance) for concordance in content]
    with open(path_to_file, 'w') as file:
        file.write('\n'.join(list_strings))


def sort_concordance(tokens: list, word: str, left_context_size: int, right_context_size: int, left_sort: bool) -> list:
    """
    Gets a concordance of a word and sorts it by either left or right context
    :param tokens: a list of tokens
    :param word: a word-base for a concordance
    :param left_context_size: the number of words in the left context
    :param right_context_size: the number of words in the right context
    :param left_sort: if True, sort by the left context, False – by the right context
    :return: a concordance
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy',
                    'the', 'dog', 'is', 'happy', 'but', 'the', 'cat', 'is', 'sad']
    word = 'happy'
    left_context_size = 2
    right_context_size = 3
    left_sort = True
    --> [['dog', 'is', 'happy', 'but', 'the', 'cat'], ['man', 'is', 'happy', 'the', 'dog', 'is']]
    """
    if not isinstance(left_sort, bool):
        return []
    if isinstance(left_context_size, int) and left_context_size < 0 and not left_sort:
        left_context_size = 0
    if isinstance(right_context_size, int) and right_context_size < 0 and left_sort:
        right_context_size = 0

    concordance = get_concordance(tokens, word, left_context_size, right_context_size)
    if len(concordance) == 0:
        return []

    if left_sort:
        dict_raw = {context[0]: context for context in concordance}
    else:
        dict_raw = {context[context.index(word)+1]: context for context in concordance}
    list_output = [dict_raw[key] for key in sorted(dict_raw)]
    return list_output
