
from urllib import request
import re

re_list=re.compile(r'<a href="(.*html)" onclick=.* class=.*s xst.*>(.*)</a>')
re_img=re.compile(r'<img id=.* aid=.*zoomfile="(.*)" file=.* class="zoom" .*onmouseover=.* />')


def get_one_page(pageurl):

    with request.urlopen(pageurl) as imglist:
        data=imglist.read()
        print(data.decode('utf-8'))
##        print(re_img.findall(data.decode('utf-8')))

def get_pagelist(mainpage):
    return re_list.findall(mainpage)
hosturl='http://www.example.com/forum-98-1.html'
with request.urlopen(hosturl) as f:
    data=f.read()
##    with open('d:\\text.html','wb') as ff:
##        ff.write(data)
##    print(data.decode('utf-8'))
    pagelist=get_pagelist(data.decode('utf-8'))
    print(pagelist[0])
    get_one_page(pagelist[0][0])
##    for page in pagelist:
##        get_one_page(page)
