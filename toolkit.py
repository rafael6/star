#!/usr/bin/env python3

__author__ = 'rafael'
__version__ = '4.1.0'

"""
This modules provides methods for checking: DNS, ICMP, sockets, and URL status.

>>> import toolkit
>>> hostname = 'yahoo.com'
>>> print(toolkit.check_dns(hostname, ['8.8.8.8'], 'a'))
206.190.36.45, 98.139.183.24, 98.138.253.109
>>> print(toolkit.check_ping(hostname, '4'))
--- yahoo.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 602ms
rtt min/avg/max/mdev = 100.700/103.932/111.040/4.159 ms
>>> print(toolkit.check_socket(hostname, 80, 'tcp'))
open
>>> print(toolkit.check_url('https://yahoo.com'))
200
"""

import dns.resolver
import socket
import subprocess
import urllib.request


def check_dns(node, nservers, qtype):
    """
    Process name resolution (DNS) queries on a given node (hostname or IP)
    using a name server from a given list of name servers (nservers), and a
    query type (qtype). Returns DNS data otherwise an exception.

    Example:
        import toolkit
        print(toolkit.check_dns(yahoo.com, ['8.8.8.8'], 'a'))

    :param node: string, IP address or hostname in DNS.
    :param nservers: list of strings, DNS servers.
    :param qtype: string, one of the these query types: A/CNAME, MX, PTR.
    :return: string, name resolution data otherwise an exception.
    """
    try:
        _resolver = dns.resolver.Resolver()
        _resolver.nameservers = nservers
        if qtype.lower() == 'mx':
            _answer = _resolver.query(node, qtype)
            _data = ['Host {} preferance {}'.format(
                rdata.exchange, rdata.preference) for rdata in _answer]
        elif qtype.lower() == 'ptr':
            _answer = _resolver.query(dns.reversename.from_address(node), qtype)
            _data = [str(record) for record in _answer]
        else:
            # Handles both A and CNAME records
            #_answer = _resolver.query(node, qtype)
            _data = [str(address) for address in _resolver.query(node, qtype)]
    except dns.exception.SyntaxError:
        return 'Error; check IP address.'
    except dns.rdatatype.UnknownRdatatype:
        return 'Error; check query type.'
    except dns.resolver.NoAnswer:
        return 'Error; check query type.'
    except dns.resolver.NXDOMAIN:
        return 'Error; check hostname.'
    except dns.exception.Timeout:
        return 'Timeout; check connection and DNS server.'
    else:
        return ', '.join(_data)


def check_ping(node, count='9'):
    """
    Pings node (IP address or hostname) with a load of 1378 bytes, with a given
    number of times (9 by default), at a 200ms interval. Returns a ping
    statistics as a string otherwise an exception.

    Example:
        import toolkit
        print(toolkit.check_ping('google.com', '4'))

    :param node: string, IP address or hostname in DNS.
    :param count: string, number of echo requests.
    :return: string, containing ping related information or an exception.
    """
    _interval = '.2'  # 200ms
    _size = '1350'    # bytes
    _command = 'ping -c {} -i {} -s {} {} | grep -1 loss'.format(
        count, _interval, _size, node)
    try:
        output = subprocess.check_output(_command, shell=True).decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        return str(e)
    else:
        return output


def check_socket(node, port, kind='tcp'):
    """
    Check the status of a given socket using node, port, and kind as arguments.
    Returns 'open' is the socket is open otherwise an exception.

    Example:
        import toolkit
        print(toolkit.check_socket('yahoo.com', 80, 'tcp'))

    :param node: string, IP address or hostname in DNS.
    :param port: integer, TCP/UDP port number.
    :param kind: string, port type TCP or UDP.
    :return: string, open otherwise and exception.
    """
    if kind.lower() == 'udp':
        _sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    else:
        _sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        _sock.connect((node, port))
        _sock.close()
    except socket.error as e:
        return str(e)
    except OverflowError as e:
        return str(e)
    else:
        return 'open'


def check_url(url):
    """
    Check the status of a given URL and returns the HTTP code as a string.
    Returns the HTTP status code otherwise an exception.

    Example:
        import toolkit
        print(toolkit.check_url('https://yahoo.com'))

    :param url: string, URL/URI to check.
    :return: string, HTTP code otherwise and exception.
    """
    try:
        _connection = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        return str(e)
    except ValueError as e:
        return str(e)
    except ConnectionResetError as e:
        return str(e)
    else:
        return str(_connection.getcode())


def main():
    hostname = 'yahoo.com'
    print(check_dns(hostname, ['8.8.8.8'], 'a'))
    print(check_ping(hostname, '3'))
    print(check_socket(hostname, 80, 'tcp'))
    print(check_url('https://yahoo.com'))

if __name__ == "__main__":
    main()
