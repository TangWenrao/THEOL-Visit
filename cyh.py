import urllib.request,urllib.error,urllib.parse
import http.client 
test_data = {'lessId':'12927'}
test_data_urlencode = urllib.parse.urlencode(test_data)

requrl = "https://course-proxy2.buct.edu.cn/meol/lesson/onlinetime_listener.jsp"
headerdata = {
    "Host":"course-proxy2.buct.edu.cn",
    "Cookie" : "JSESSIONID=899B1F4301D80DEEAC7D0D8676A0D2E0.TM1; DWRSESSIONID=fJuETH3tPXdPrqDAEQM072DtA7n; _ga=GA1.3.1550904115.1580626844; Hm_lvt_ad849b6d5c2eae8de079e3913855d1ff=1587368734,1587445302,1587521991,1587602191; _gid=GA1.3.299344480.1587345716; Hm_lpvt_ad849b6d5c2eae8de079e3913855d1ff=1587620594",
    "Origin" : "https://course-proxy2.buct.edu.cn",
    "Referer": "https://course-proxy2.buct.edu.cn/meol/jpk/course/layout/newpage/index.jsp?courseId=12927",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate, br',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Content-Length':'12',
    'TE	':'Trailers',
    'X-Requested-With':'XMLHttpRequest'
    }

conn = http.client.HTTPConnection("121.195.154.239:443")

conn.request(method="POST",url=requrl,body=test_data_urlencode,headers = headerdata) 

response = conn.getresponse()

res= response.read()
response.close()
print(res)
