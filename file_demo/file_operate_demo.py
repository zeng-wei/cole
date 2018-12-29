# 需求：从api_client.log、api_client1.log、api_client2.log读取日志，按test.xlsx文件的号码顺序生成新的log文件
import xlrd
import re
import collections


base_path = './file_demo/'

print('operate start')
table = xlrd.open_workbook(base_path+'test.xlsx').sheets()[1]
data = collections.OrderedDict()
for phone in table.col_values(0):
    data[phone] = []


def add_data_from_log_file(file_name):
    with open(base_path+file_name) as f:
        while True:
            content = f.readline()
            if not content:
                break
            match_obj = re.search(".*?resultJsonData=(.*)", content)
            if match_obj:
                try:
                    item = eval(match_obj.groups()[0])
                    phone = item['returnVo']['data']['tel']
                    data[phone].append(item['returnVo']['data'])
                except Exception:
                    print(content)
                    continue
            else:
                try:
                    item = eval(content)
                    phone = item['data']['tel']
                    data[phone].append(item['data'])
                except Exception:
                    print(content)
                    pass


add_data_from_log_file('api_client.log')
add_data_from_log_file('api_client1.log')
add_data_from_log_file('api_client2.log')

with open('new.log', 'w') as f:
    for content_list in data.values():
        for content in content_list:
            f.write(str(content)+'\n')

print('operate finish! to ---> new.log')