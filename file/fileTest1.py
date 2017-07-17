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



f = open("yesterday", encoding='utf-8')

print(f.read())
print('------------------------------')
print(f.read())