#!/usr/bin/python

__author__ = 'Rafael'

from toolkit import Toolkit
import time

def main():
    hostnames = ['google.com', 'yahoo.com']
    urls = ['http://hg.secdev.org']
    ports = [80, 443]
    nodes = ['localhost']
    commands = ['whoami']
    username = ''
    password = ''

    print '>>>Running System Test; please wait...'
    print '>>>Press Ctrl+C to exit.'
    time.sleep(5)

    print '>>>Checking DNS and ICMP...'
    print '>>>The average RTT should be less than 5ms with 0% packet loss.'
    print
    tool = Toolkit(hostnames)
    tool.process_host()

    print '>>>Checking sockets...'
    print '>>>The sockets listed should be open.'
    tool = Toolkit(hostnames, ports)
    tool.process_socket()

    print
    print '>>>Checking URLs...'
    print '>>>The URLs listed should return a 200 code.'
    tool = Toolkit(urls)
    tool.process_url()

    print
    print '>>>SSH session...'
    tool = Toolkit(nodes, commands, username, password)
    tool.process_ssh()

if __name__ == "__main__":
    main()
