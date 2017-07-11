
p = [['alex', [100, 30]], ['jim', [200, 400]], ['ann', [400, 50]]]

for name, age in p:
    print name, age

index = []


def add_to_index(index, keyword, url):
    for p in index:
        if keyword == p[0]:
            p[1].append(url)
            return

    index.append([keyword, [url]])