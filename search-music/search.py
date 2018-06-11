#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#

import requests, bs4

search_index = 'http://so.5nd.com'


def searchMusic(k):
    response = requests.get(search_index + '/k_' + k)
    soup = bs4.BeautifulSoup(response.text)
    aList = soup.select('ul.mulist a[href^=http://www.5nd.com/ting/]')
    url = []
    for a in aList:
        print(a.getText(), a.attrs['href'])
        # url.append({
        #   url: a.attrs['href']
        #   title: a.attrs['title']
        # })
        url.append(a.getText() + '"' + a.attrs['href'] + '"')
    return url
