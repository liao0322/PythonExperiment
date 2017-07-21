import file


'''
with open('yesterday', encoding='utf-8') as f:
    print(f.tell())
    for line in f:
        print(line, end='')

    print('\n%d' % f.tell())

    f.seek(90)
    # print('\n%d' % f.tell())
    print(f.readline())

'''



with open("yesterday", 'r', encoding='utf-8') as f, \
    open("yesterday2", 'w', encoding='utf-8') as f2:

    for raw in f:
        if "生命" in raw:
            raw = raw.replace("生命", "life")
        f2.write(raw)





