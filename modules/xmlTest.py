import requests

from xml.etree import ElementTree as ET

# 检查指定的QQ号是否在线
'''
response = requests.get('http://ws.webxml.com.cn/webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=185489684')

node = ET.XML(response.text)

if node.text == 'Y':
    print('在线')
else:
    print('离线')
'''

# 获取列车时刻表
'''
response = requests.get('http://ws.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=g102&UserID=')
node = ET.XML(response.text)
'''

root = ET.XML(open('test.xml', 'r', encoding='utf-8').read())

for node in root:
    print(node.tag, node.attrib, node.find('year').text)


