import requests
import time
from threading import Thread
from requests.adapters import HTTPAdapter
import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}

session = requests.session()
session.mount('https://', HTTPAdapter(pool_connections=2, pool_maxsize=100))  # 增加连接池


def http_request(url):
    try:
        webPage = session.get(url, headers=headers)
        html = webPage.text
        return {"context": html}
    except Exception as e:
        return {"error": e}


def run():
    threads = []
    t = time.time()
    tasks_num = 100
    for x in range(tasks_num):
        url = "https://www.baidu.com"
        url1 = "https://www.zhihu.com/question/36612174"
        # 多线程执行requests, 当url有多个host, pool_connections小于host数量时, 在切换host的时候requests会打开一个新的connection
        # 多线程执行requests, 设置pool_maxsize为线程数量来发送请求, 不然容易出现Connection pool is full, discarding connection的错误
        thread = Thread(target=http_request, args=(url,))
        threads.append(thread)
        thread.start()
        thread = Thread(target=http_request, args=(url1,))
        threads.append(thread)
        thread.start()
    for i in threads:
        i.join()
    print("Multi thread execute %s Http request spend time %ss" % (tasks_num * 2, time.time() - t))


if __name__ == '__main__':
    run()