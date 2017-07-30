from crawler_util import page_read
import random


class Proxies(object):
    def __init__(self):
        self.proxies = list()
        self.maintain_ip()

    def maintain_ip(self):
        self.proxies = list()
        soup = page_read.page_read_nolog("http://www.free-proxy-list.net/")
        tbody = soup.find_all('tbody')[0]
        for row in tbody.find_all('tr'):
            proxytem = {"http": "http://" + row.find_all('td')[0].get_text() + ":" + row.find_all('td')[1].get_text()}
            self.proxies.append(proxytem)

    def random_ip(self):
        if len(self.proxies) < 20:
            return self.proxies[random.randint(0, len(self.proxies) - 1)]
        else:
            return self.proxies[random.randint(0, 20)]

    def delete_ip(self, invalid_ip):
        if len(self.proxies) < 4:
            self.maintain_ip()
        else:
            self.proxies.remove(invalid_ip)
