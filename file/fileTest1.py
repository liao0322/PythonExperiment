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



with open("yesterday", 'r+', encoding='utf-8') as f:
    for raw in f:
        if '不知为何' in raw:
            raw = raw[4:]

        print(raw, end='')




