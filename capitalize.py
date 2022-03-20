def correct_sentence(text: str) -> str:
    text.replace(text[0], text[0].upper(),1)
    if text[-1] != '.':
        text = text+'.'
    return print(text)



correct_sentence("greetings, friends")


#solution
def correct_sentence(text: str) -> str:
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")