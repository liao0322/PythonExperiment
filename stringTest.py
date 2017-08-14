#coding:utf-8

str = '''</b><a href="http://news.baidu.com/ns?cl=2&rn=20&tn=news&word=" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'news'})">新闻</a><a href="http://tieba.baidu.com/f?kw=&fr=wwwt" wdfield="kw"  onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a><a href="http://zhidao.baidu.com/q?ct=17&pn=0&tn=ikaslist&rn=10&word=&fr=wwwt" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a><a href="http://music.baidu.com/search?fr=ps&ie=utf-8&key=" wdfield="key"  onmousedown="return c({'fm':'tab','tab':'music'})">音乐</a><a href="http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'pic'})">图片</a><a href="http://v.baidu.com/v?ct=301989888&rn=20&pn=0&db=0&s=25&ie=utf-8&word=" wdfield="word"   onmousedown="return c({'fm':'tab','tab':'video'})">视频</a><a href="http://map.baidu.com/m?word=&fr=ps01000" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'map'})">地图</a><a href="http://wenku.baidu.com/search?word=&lm=0&od=0&ie=utf-8" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'wenku'})">文库</a><a href="//www.baidu.com/more/"  onmousedown="return c({'fm':'tab','tab':'more'})">更多»</a>
</div>'''

print str.find('"', str.find('<a href='))


# find 用法
str = 'hello world'

# 没找到返回-1
index = str.find('a')
print(index)