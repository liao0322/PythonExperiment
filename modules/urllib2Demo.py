
from urllib import request

a = []

for i in range(5701430, 9999999):
    url = 'http://www.cnblogs.com/yuanchenqi/articles/%d.html' % i
    try:
        with request.urlopen(url) as f:
            if f.status == 200:
                print(url)
    except:
        pass



'''
with request.urlopen('http://www.cnblogs.com/yuanchenqi/articles/5830025.html') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    #print('Data:', data.decode('utf-8'))
'''
