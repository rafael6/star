#!/usr/bin/python

__author__ = 'Rafael'
import getpass
from toolkit import Connect
from toolkit import Toolkit
import time


def main():
    hostnames = ['google.com', 'yahoo.com']
    urls = ['http://hg.secdev.org']
    ports = [80, 443]
    nodes = ['192.168.0.8', '192.168.186.1']
    commands = ['whoami', 'ls']

    print '>>>Running System Test; please wait...'
    print '>>>Press Ctrl+C to exit.'
    time.sleep(5)

    print '>>>Checking DNS and ICMP...'
    print '>>>The average RTT should be less than 5ms with 0% packet loss.'
    for hostname in hostnames:
        tool = Toolkit(hostname)
        print tool.check_host()

    print '>>>Checking sockets...'
    print '>>>All the sockets listed below should be open.'
    for hostname in hostnames:
        for port in ports:
            tool = Toolkit(hostname, port)
            print tool.check_socket()

    print '>>>Checking URLs...'
    print '>>>The the URLs listed below should return a 200 code.'
    for url in urls:
        tool = Toolkit(url)
        print tool.check_url()

    print '>>>SSH session...'
    username = raw_input('Enter your username: ')
    password = getpass.getpass()
    for node in nodes:
        connect = Connect(node, commands, username, password)
        print connect.ssh()


if __name__ == "__main__":
    main()
