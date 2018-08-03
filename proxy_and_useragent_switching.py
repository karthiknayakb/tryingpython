#from lxml.html import fromstring
import requests
from itertools import cycle
#import traceback
 
def get_proxies():
    url = 'https://proxy.l337.tech/txt'
    response = requests.get(url)
    parser = response.text.split("\n")
    proxies = []
    for i in parser:
        if i:
            proxies.append("http://"+str(i))
    return proxies

def get_url(url,proxy,user_agent):
    response = requests.get(url1,proxies=proxie,headers=user_agent,timeout=10)
    return response

user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]
 
# #If you are copy pasting proxy ips, put in the list below
#proxies = ['http://185.93.204.132:41258']
proxies = get_proxies()
# #print proxies
proxy_pool = cycle(proxies)
user_agent_pool = cycle(user_agent_list)
# # for i in range(30):
# #     print next(proxy_pool)

url1 = 'https://httpbin.org/ip'
url2 = 'https://httpbin.org/user-agent'
for i in range(1,11):
    #Get a proxy from the pool
    #next(proxy_pool)
    print("Request #%d"%i)
    try:
        proxie = {
            'http': next(proxy_pool),
            'https': next(proxy_pool),
        }
        user_agent = {
            'User-Agent': next(user_agent_pool)
        }
        print("proxies= ",proxie)
        response = requests.get(url1,proxies=proxie,headers=user_agent)
        print(response.json())
        response = requests.get(url2,proxies=proxie,headers=user_agent)
        print(response.json())
    except Exception as e:
    #     #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
    #     #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
         print("Skipping. Connnection error ")

