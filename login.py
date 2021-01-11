import requests
import time

def login():
	url = "www.baidu.com"
	data = {"user":"admin",
			"password":"admin999"
			}
	headers = ""
	response = requests.post(url=url,data=data,headers=headers)
	asaert response.status_code == 204

if __name__== "__main__":
	login()
	


