
text = 'No [b]hi'
begin ='[b]'
end = '[/b]'


b = text.find(begin)
e = text.find(end)
if b != -1 and e != -1:
    print( text[b + len(begin):e])
elif b == -1 and e != -1:
    print( text[:e])
elif b != -1 and e == -1:
    print( text[b+ len(begin):])
elif b == -1 and e == -1:
    print( text)



def between_markers(text: str, begin: str, end: str) -> str:
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]