import redis
import requests
from multiprocessing import Process

def ver_test(t):
    try:
        url = "http://www.baidu.com/"
        t = "http://" + str(t.decode('UTF-8'))
        proxies = {"http": t}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        }
        res = requests.get(url, proxies=proxies, headers=headers)
        return True
    except:
        return False

def main():
    db = redis.Redis(host='127.0.0.1',port='6379',db=5)
    while db.llen('ip') > 0:
        t = db.lpop('ip')
        # print(str(t.decode('UTF-8')))
        if ver_test(t):
            print(t.decode('UTF-8'),'YES')
            db.rpush('ip',t)
        else:
            print(t.decode('UTF-8'),'NO')

if __name__ == '__main__':
    for i in range(0,50):
        s = str('pro_' + str(i))
        s = Process(main())
        s.start()