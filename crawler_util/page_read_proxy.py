# import ipScrape
from bs4 import BeautifulSoup
import requests
import logging
import traceback


def page_read_proxy_inner(target_url, proxy):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    }

    try:
        html = requests.get(target_url, proxies=proxy, headers=headers, timeout=10)
        # soup = BeautifulSoup(html.text.encode(html.encoding).decode('utf-8'), 'lxml')  #Chinese
        soup = BeautifulSoup(html.text, 'lxml')
        return soup
    except Exception as e:
        # pass
        logging.error(traceback.format_exc())
        print 'cannot open the page'


# def page_read_proxy(target_url):
#     i = 0
#     the_proxy = ip_scrape.random_ip()
#     soup = page_read_proxy_inner(target_url, the_proxy)
#     while i < 5 and not soup:
#         ip_scrape.delete_ip(the_proxy)
#         the_proxy = ip_scrape.random_ip()
#         soup = page_read_proxy_inner(target_url, the_proxy)
#         i += 1
#     while i < 10 and not soup:
#         ip_scrape.maintain_ip()
#         soup = page_read_proxy_inner(target_url, ip_scrape.random_ip())
#         i += 1
#     if not soup:
#         print 'maybe no network or invalid website'
#     else:
#         return soup


# ip_scrape = ipScrape.Proxies()
