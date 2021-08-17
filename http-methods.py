#Printing out each of the methods that are supported by a given web-server

import requests

list_methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'TEST']
for method in list_methods:
  req = requests.request(method, 'https://www.bing.com')
  print(method, req.status_code, req.reason)

