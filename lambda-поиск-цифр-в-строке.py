sum_numbers = lambda text: sum(int(word) for word in text.split() if word.isdigit())

# через фильтр
def sum_numbers(text: str) -> int:
    return sum(map(int, filter(str.isdigit, text.split())))