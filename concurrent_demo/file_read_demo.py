# 批量文件读取demo，/Users/zhhnzw/Downloads/PX路径下有1w个文件，共13GB
from threading import Thread
import queue
import os
import json
import time


base_path = '/Users/zhhnzw/Downloads/PX'

tasks = queue.Queue()


def load_tasks():
    for i in os.listdir(base_path):
        tasks.put(i)


def read_file(file_name):
    with open(base_path+'/'+file_name) as f:
        content = f.readlines()
        return content


def handle_content(content):
    for i in content:
        obj = json.loads(i)
        # print(obj)


def handle():
    while tasks.empty() is False:
        try:
            file_name = tasks.get(timeout=0.1)
        except queue.Empty:
            break
        print(file_name, 'remain task num:', tasks.qsize())
        content = read_file(file_name)
        handle_content(content)
    print('-------------------- end --------------------')


def run():
    begin = time.time()
    load_tasks()
    threads = []
    for x in range(1024):
        thread = Thread(target=handle)
        threads.append(thread)
        thread.start()
    for i in threads:
        i.join()
    end = time.time()
    print(f'pass time:{end-begin}')


if __name__ == '__main__':
    run()