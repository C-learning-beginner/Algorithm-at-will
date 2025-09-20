"""
#连接到浏览器
from DrissionPage import ChromiumOptions
path =r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
ChromiumOptions().set_browser_path(path).save()
"""
import re
import requests
#打开浏览器
from DrissionPage import ChromiumPage
#把浏览器对象赋值给dp
dp = ChromiumPage()
"""
1.监听数据包(实际上是过滤网页内容)
2.访问网站
3.等网站加载
4.获取数据
5.解析数据(py知识)
"""



#1监听数据包
dp.listen.start('lianxiti')


#2访问网站
dp.get('https://www.jsyks.com/kms-sxlx')


#3等待数据包加载
r = dp.listen.wait()


#4获取数据
info = r.response.body
#print(info)

"""5解析数据"""

answer_id_list = re.findall('var ExamCodes = "(.*?)";', info)[0].split(',')
print(answer_id_list)

for answer_id in answer_id_list:
    answer_url = f'https://tiba.jsyks.com/Post/{answer_id}.htm'
    html = requests.get(url = answer_url).text
    #answer = re.findall()
    answer = re.findall('答案是：(.*?)。',html)[0]
    for a in answer:
        if a == 'A':
            dp.ele('css:#inA').click()
        elif a =='B':
            dp.ele('css:#inB').click()
        elif a =='C':
            dp.ele('css:#inC').click()
        elif a =='D':
            dp.ele('css:#inD').click()
        elif a =='对':
            dp.ele('css:#inRight').click()
        else:
            dp.ele('css:#inErr').click()
    dp.ele('css:#btn_PN span').click()


"""
list =dp.eles('css:div.Exam li')
for i in list:
    answer = i.attr('k')
    #有多选，要循环answer
    for a in answer:
        if a == 'R':
            i.ele('css:b:nth-child(3)').click()
        elif a =='E':
            i.ele('css:b:nth-child(4)').click()
        elif a == 'A':
            i.ele('css:b:nth-child(3)').click()
        elif a == 'B':
            i.ele('css:b:nth-child(4)').click()
        elif a == 'C':
            i.ele('css:b:nth-child(5)').click()
        else:
            i.ele('css:b:nth-child(6)').click()
    print(answer)
#定位提交试卷按钮
dp.ele('css:btnJJ').click()
"""


