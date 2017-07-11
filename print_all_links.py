#coding:utf-8

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

def get_all_links(page):
    urls = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            urls.append(url)
            page = page[endpos:]
        else:
            break
    return urls

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0

    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return url, end_quote

page = get_page('http://xkcd.com/353')
print_all_links(page)


def crawl_web(seed):
    to_crawl = [seed]
    crawled = []

    while to_crawl:
        url = to_crawl.pop()
        if url not in crawled:
            page = get_page(url)
            union(to_crawl, get_all_links(page))
            crawled.append(url)


    return crawled

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)