'''EN Russian
Ваша задача в этой миссии определить популярность определенных слов в тексте.

На вход вашей функции передается 2 аргумента. Текст и массив слов, популярность которых необходимо определить.

При решении этой задачи обратите внимание на следующие моменты

Слова необходимо искать во всеx регистрах. Т.е. если необходимо найти слово "one", значит для него будут подходить слова "one", "One", "oNe", "ONE" и.т.д.
Искомые слова всегда указаны в нижнем регистре
Если слово не найдено ни разу, то его необходимо вернуть в словаре со значением 0 (ноль)
Входные параметры: Текст и массив искомых слов.

Выходные параметры: Словарь, в котором ключами являются искомые слова и значениями то, сколько раз они встречаются в исходном тексте.

# Пример:'''


def popular_words(text: str, words: list) -> dict:
    answer = {}

    t = list(text.replace('\n', ' ').split(' '))
    for x in words:
        answer[x] = 0
        for element in t:
            if x == element.lower():
                answer[x] = answer.get(x, 0) + 1

    return answer


def popular_words(text, words):
    lower_count = text.lower().split().count
    return {word: lower_count(word) for word in words}

def popular_words(text, words):
    counter = {word: 0 for word in words}
    for word in text.lower().split():
        if word in counter:
            counter[word] += 1
    return counter

asas = {'a': 1, 'b': 2}
asas['b'] = asas.get('b', 0) + 1

print(asas.get('b'))

text = 'When I was One ' \
       'I had just begun' \
       'When I was Two' \
       'I was nearly new'

t = list(text.split())

print(t)


