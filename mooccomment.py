import urllib.parse
import urllib.request

url='http://www.imooc.com/course/docomment'
postdata=urllib.parse.urlencode({'content':'测试一下自动提交的内容',
    'mid':'8837'})
postdata=postdata.encode('utf-8')


headers={
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection':'keep-alive',
    'Content-Length':len(postdata),
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'Host':'www.imooc.com',
    'Origin':'http://www.imooc.com',
    'Referer':'http://www.imooc.com/video/8837',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}
req = urllib.request.Request(url)
for k in headers:
    req.add_header(k,headers[k])

with urllib.request.urlopen(req,postdata) as f:
    print('status:%s'%f.status)