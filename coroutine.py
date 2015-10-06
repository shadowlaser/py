__author__ = 'Administrator'

def consumer():
    r=''
    while True:
        print('while start')
        print('r===%s'%r)
        n=yield r
        print('n==%s'%n)
        if not n:
            return
        print('Consumer consuming %s'%n)
        r='200 OK'

def produce(c):
    c.send(None)
    n=0
    while n<5:
        n=n+1
        print('procuding...%s'%n)
        r=c.send(n)
        print('consumer return:%s'%r)

    c.close()

c=consumer()
produce(c)