#!/usr/bin/env python
import requests
import re
from urllib.parse import urljoin
def request(url):
    try:
        get_response = requests.get(url)
        return get_response
    except Exception:
        pass

def extract_links(url):
    response = request(url)
    return re.findall('(?:href=")(.*?)"', str(response.content))


include_url = []
exclude_url = []
target_url = "https://zsecurity.org/"

href_links = extract_links(target_url)
print(len(href_links))
# print(href_links)
for link in href_links:
    if target_url in link:

        link = urljoin(target_url, link)
        include_url.append(link)
        # print(link)
    else:
        exclude_url.append(link)


print(include_url)
print(exclude_url)


