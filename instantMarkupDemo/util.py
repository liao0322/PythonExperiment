def lines(file):
    '''在文件的最后追加一个空行'''
    for line in file: yield line
    yield '\n'

def blocks(file):
    '''根据空行给文本分块'''
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
