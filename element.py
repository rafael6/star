#!/usr/bin/env python3

__author__ = 'rafael'
__version__ = '3.3.0'

"""
Dispatch and format output.

>>> import element
>>> element_ = 'yahoo.com'
>>> print(element.get_element(element_))
        Element: yahoo.com
>>> print(element.get_etype('Web Server'))
                Type: Web Server
>>> print(element.get_dns(element_, ['8.8.8.8'], 'a'))
                DNS a records: 98.139.183.24, 98.138.253.109, 206.190.36.45
>>> print(element.get_ping(element_))
                Ping: 0% packet loss
>>> ports = (80, 443)
>>> for port in element.get_socket(element_, ports, 'tcp'):
...     print(port)
...
                tcp port 80: open
                tcp port 443: open
>>> urls = ('https://yahoo.com', 'http://yahoo.com')
>>> for url in element.get_url(urls):
...     print(url)
...
                URL https://yahoo.com: 200
                URL http://yahoo.com: 200

"""

__author__ = 'rafael'

import toolkit
import timeit


def get_dns(node, nservers, qtype):
    """
    Calls toolkit's check_dns() function and formats its ouput for display.

    :param node: string, IP address or hostname in DNS.
    :param nservers: list of strings, list of DNS servers.
    :param qtype: string, type of record such as A, PRT, CNAME, or MX.
    :return: string, formatted Toolkit's check_dns() output.

    Example:
        import element
        print(element.get_dns('google.com', [8.8.8.8], 'a'))
    """
    return '\t\tDNS {} records: {}'.format(
        qtype, toolkit.check_dns(node, nservers, qtype))


def get_ping(node):
    """
    Calls Toolkit's check_host(node) function and filter the returned value
    to capture just the packet loss portion. Returns the packet loss counter.

    :param node: string, IP address or hostname in DNS.
    :return: string, formatted Toolkit's check_host packet-loss counter.

    Example:
        import element
        print(element.get_host('google.com'))
    """
    output = toolkit.check_ping(node)
    try:
        filter = output.split('received, ')[1]  # filter
        refined = filter[0:16].strip(', ')      # 0% packet loss
        return '\t\tPing: {}'.format(refined)
    except IndexError:
        return 'connection error'


def get_socket(node, ports, kind):
    """
    Calls Toolkit's check_socket() function for each element (port) in the
    container list/tuple. Formats the returned value as such:
    'TCP port 80: open'.

    :param node: string, IP address or hostname in DNS.
    :param ports: container list/tuple, containing integers (TCP/UDP ports).
    :param kind: string, port type TCP or UDP.
    :return: generator object

    Example:
        import element
        element.get_socket('google.com', [80, 443], 'tcp')
    """

    """
    # This generator would be a better choice for large data sets.
    for port in ports:
        result = toolkit.check_socket(node, port, kind)
        port_stat = '\t\t{} port {}: {}'.format(kind, port, result)
        yield port_stat

    """
    return ['\t\t{} port {}: {}'.format(kind, port, toolkit.check_socket(
        node, port, kind)) for port in ports]


def get_url(urls):
    """
    Calls Toolkit's check_socket() function for each URL in container urls.
    Format the returned value as such: 'URL http://yahoo.com: open'.

    :param urls: container, list or tuple containing strings for each URL/URI
    :return: generator object

    Example:
        import element
        element.check_url(['https://google.com', http://yahoo.com'])
    """
    """
    # This geneartor would be a better option for large data sets.
    for url in urls:
        result = toolkit.check_url(url)
        url_stat = '\t\tURL {}: {}'.format(url, result)
        yield url_stat
    """
    return ['\t\tURL {}: {}'.format(url, toolkit.check_url(url)) for url in urls]


def get_element(node):
    """
    Formats variable node for display.

    :param node: string, IP address or hostname in DNS.
    :return: string, formatted string output.

    Example:
        import element
        element.get_element('google.com')
    """
    return '\tElement: {}'.format(node)


def get_etype(etype):
    """
    Format variable etype for display.

    :param etype: string, element type such as F5, Server, etc.
    :return: string, formatted string output.

    Example:
        import element
        element.get_etype('Web Server')
    """
    return '\t\tType: {}'.format(etype)


def main():
    resolvers = ['8.8.8.8']
    query_type = 'a'
    ports = (80, 443)
    port_type = 'tcp'
    urls = ('https://yahoo.com', 'http://yahoo.com')

    print('Checking application my.app.com; please wait...')

    element_ = 'yahoo.com'
    print(get_element(element_))
    print(get_etype('Web Server'))
    print(get_dns(element_, resolvers, query_type))
    print(get_ping(element_))
    for output in get_socket(element_, ports, port_type):
        print(output)
    for url in get_url(urls):
        print(url)

if __name__ == '__main__':
    #timeit.main()
    main()
