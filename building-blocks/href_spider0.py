#!/usr/bin/env python
import requests
import re

def request(url):
    try:
        get_response = requests.get(url)
        return get_response
    except Exception:
        pass


url = "http://ajwapaste.com.pk"

response = request(url)
print(type(response.content))
# content = str(response.content)
# print(type(content))
href_links = re.findall('(?:href=")(.*?)"', str(response.content))
print(type(href_links))
print(href_links)
for link in href_links:
    print(link)
