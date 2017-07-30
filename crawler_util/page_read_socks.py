# encoding=utf-8
import urllib2
from bs4 import BeautifulSoup
import socks
from sockshandler import SocksiPyHandler
import logging
import traceback


def page_read_sock_inner(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    }
    request = urllib2.Request(url, None, headers)
    try:
        x = opener.open(request, timeout=10)
        return BeautifulSoup(x.read(), 'lxml')
    except:
        logging.error(traceback.format_exc())


def page_read_sock(myurl):
    i = 0
    soup = page_read_sock_inner(myurl)
    while not soup and i < 5:
        i += 1
        print myurl + 'try open again'
        soup = page_read_sock_inner(myurl)
    return soup


opener = urllib2.build_opener(SocksiPyHandler(socks.SOCKS5, "127.0.0.1", 1080))
