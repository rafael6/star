__author__ = 'Rafael'

import os
import time
import subprocess
from toolkit import Toolkit

#VIPs
vips = ['vip.mycorp.com']
#VIP Members:
hosts_vip = ['member1.mycorp.com', 'member2.mycorp.com']
#TCP/UDP ports:
ports_http = [80, 443]
#URLs
urls = ['https://myapp.mycorp.com', 'http://myapp.mycorp.com']
# Messages
MSG_START = '''Running SYSTEM Test; please wait...
Press Ctrl+C to exit.\n'''
MSG_DNS_ICMP = '>>>Checking DNS and ICMP >>> All listed host(s) should be reachable.'
MSG_MEMBER = '>>>Checking services on the following member(s) >>> All port(s) should be open.'
MSG_VIP = '>>>Checking services on the following VIP(s) >>> All port(s) should be open.'
MSG_URL = '>>>Checking URL(s) >>> All listed URL(s) should return an HTTP code of 200.'
MSG_END = '''Test complete.
print 'If all test OK, perhaps the problem is outside of the data center.
Press Ctrl+C to exit.\n'''


def iterator(node):
    for i in node:
        tool = Toolkit(i)
        print tool.check_host()


def iter_socket(nodes, ports):
    time.sleep(5)
    for i in nodes:
        for j in ports:
            tool = Toolkit(i, j)
            print tool.check_socket()


def iter_url(urls):
    time.sleep(5)
    for i in urls:
        tool = Toolkit(i)
        print tool.check_url()


def main():
    print MSG_START
    print

    print MSG_DNS_ICMP
    iterator(vips)
    iterator(hosts_vip)

    print MSG_MEMBER
    iter_socket(hosts_vip, ports_http)
    print

    print MSG_VIP
    iter_socket(vips, ports_http)

    print
    print MSG_URL
    iter_url(urls)
    print
    print MSG_END


if __name__ == "__main__":
    main()