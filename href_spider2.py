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

def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', str(response.content))




target_urls_list = []
exclude_url = []


def crawl(url):

    href_links = extract_links_from(url)
# print(href_links)
    for link in href_links:
        links_file.write("HI Umer")
        link = urljoin(url, link)
        if "#" in link:
            link = link.split("#")[0]

        if url in link and link not in target_urls_list:
            target_urls_list.append(link)
            # print(link)
            links_file.write(link + "\n")
            crawl(link)
        else:
            exclude_url.append(link)

with open("zaid.txt","w") as links_file:
    target_url = "https://daraz.pk"
    crawl(target_url)
    print(target_urls_list)
    print(exclude_url)
