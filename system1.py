#!/usr/bin/env python3

import element

#  This a simple use case and serves as a template


def main():
    # Variable definitions here:
    resolvers = ['8.8.8.8']
    query_type = 'A'
    ports = (80, 443)
    port_type = 'TCP'
    urls = ('https://yahoo.com', 'http://yahoo.com')

    # App title
    print('Checking application my.app.com; please wait')

    # Element construct
    element_ = 'yahoo.com'
    print(element.get_element(element_))
    print(element.get_etype('Web Server'))
    print(element.get_dns(element_, resolvers, query_type))
    print(element.get_ping(element_))
    for port in element.get_socket(element_, ports, port_type):
        print(port)
    for url in element.get_url(urls):
        print(url)


if __name__ == '__main__':
    main()

