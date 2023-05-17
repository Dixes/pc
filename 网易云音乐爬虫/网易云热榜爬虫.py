import requests
import re
import os
import time
#文件夹
filename = 'music'#创建文件夹名
if not os.path.exists(filename):#判断是否存在文件夹名为music的文件夹
    os.mkdir(filename)
#获取网易云热歌榜地址
url_1= 'https://music.163.com/discover/toplist?id=3778678'#热歌榜url
url_2= 'https://music.163.com/discover/toplist?id=3779629'#新歌榜url
url_3= 'https://music.163.com/discover/toplist?id=2884035'#原创榜url
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}#设置伪装头，让程序模拟浏览器
a=int(input('请输入想下载的榜单1(热歌榜)，2(新歌榜)，3(原创榜)'))
if a == 1:
    response = requests.get(url=url_1, headers=headers)
elif a == 2:
    response = requests.get(url=url_2,headers=headers)
elif a == 3:
    response = requests.get(url=url_3,headers=headers)
#print(response.text)
html_data = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>',response.text)#正则获取歌曲id和歌名
for num_id ,title in html_data:
    time.sleep(1)#设置爬取时间间隔为1
    muisc_url=f'https://music.163.com/song/media/outer/url?id={num_id}.mp3'#连入接口获取歌曲的mp3格式地址
    muisc_content=requests.get(url=muisc_url, headers=headers).content#获取歌曲的下载
    with open(filename + '/' + title + '.mp3',mode='wb') as f:#将歌曲爬取下载至music文件夹并用歌名命名下载为mp3格式
        f.write(muisc_content)
    print('已下载歌曲：'+title)