def left_join(phrases: tuple) -> str:
    answer = [w.replace('right', 'left') for w in phrases]
    l = ','.join(answer)
    return l


# (",".join(phrases)).replace("right","left")


print(left_join(("left", "right", "left", "stop")))

words = ['left', 'right', 'bleft']

answer = [w.replace('left', 'rigth') for w in words]
print(','.join(answer))




