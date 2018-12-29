import requests
import time
from threading import Thread

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}

url = "http://www.tieba.com"


def http_request():
    try:
        webPage = requests.get(url, headers=headers)
        html = webPage.text
        return {"context": html}
    except Exception as e:
        return {"error": e}


def run():
    threads = []
    t = time.time()
    for x in range(100):
        thread = Thread(target=http_request)
        threads.append(thread)
        thread.start()

    for i in threads:
        i.join()
    print("Thread Http Request", time.time() - t)


if __name__ == '__main__':
    run()