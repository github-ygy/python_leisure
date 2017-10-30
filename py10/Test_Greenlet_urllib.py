#!/usr/bin/env python
# author：ygy

import gevent
from  gevent import monkey

monkey.patch_all()  #打补丁，遇i/o切换协程


from urllib.request import urlopen
import time

def func(url):
    print(" get from %s"%url)
    resp = urlopen(url)
    data = resp.read()
    print(" %d bytes get from %s " %(len(data),url))

urls = [
    'https://www.python.org/',
    'https://www.yahoo.com/',
    'https://github.com/'
]

syc_start = time.time()
for url in urls:
    func(url)
print(" syc takes ",time.time() - syc_start)


asyc_start = time.time()
gevent.joinall([
    gevent.spawn(func, 'https://www.python.org/'),
    gevent.spawn(func, 'https://www.yahoo.com/'),
    gevent.spawn(func, 'https://github.com/'),
])
print(" asyc takes ",time.time() - asyc_start)