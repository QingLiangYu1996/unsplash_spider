import requests
import re

def get_html(url):
        r=requests.get(url,verify=True)
        return r.text

def get_photo_id(word,page_num=10):
    photo_id=[]
    url='https://unsplash.com/napi/search/photos?query='+word+'&page='
    for i in range(page_num):
        html=get_html(url+str(i+1))
        photo_id+=re.findall('download":"https://unsplash.com/photos/(.*?)/download"',html)
    return set(photo_id)

def download(lists,out_file_path):
    lists=list(lists)
    url='https://unsplash.com/photos/'
    for i in range(len(lists)):
        TempJpg=requests.get(url+lists[i]+'/download',verify=True)
        try:
            with open(out_file_path+'\\'+lists[i]+'.jpg','wb') as f:
                f.write(TempJpg.content)
        except:
            continue


word='cat' #搜索单词
page_num=5 #页码深度
out_file_path='c:\\1\\'

photo_id=get_photo_id(word,page_num)
print (len(photo_id))
download(photo_id,out_file_path)