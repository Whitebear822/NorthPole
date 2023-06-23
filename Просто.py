def recurs(count):
    print(count)
    if count == 5:
        return
    recurs(count + 1)
    print(count)