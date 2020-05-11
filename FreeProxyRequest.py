#!/usr/bin/python3

#simple script utilizing FreeProxy as proxies

import re
import requests
from fp.fp import FreeProxy

url = "http://url:port"
cookies = {"cookie1_name": "cookie1_value", "cookie2_name": "cookie2_value"}
headers = {"header1_name": "header1_value","header2_name": "header2_value"}
#optional body (ie. multipart type)
data = "something"

for i in range(15):
	# timeout could be changed
	proxy = FreeProxy(timeout=1, rand=True).get()
	print(proxy)
	if (proxy != None):
		# reformat proxy value for request's "proxies" parameter
		x = re.findall(".*?:", proxy)
		str = x[0] 
		proxies = {str[0:len(str)-1]: proxy}
		# post or get
		req = requests.post(url, headers=headers, cookies=cookies, data=data, proxies=proxies)
		if "Success string" in req.text:
			print("Success")
		else:
			print("Fail")



	
	
