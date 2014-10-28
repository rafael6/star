#!/usr/bin/python

__author__ = 'Rafael'

import re
import socket
import subprocess
import urllib2
import paramiko

class Toolkit(object):
    """
    Provides methods the following methods:
        process_host() process a hostname list; returns DNS, loss, & latency
        process_socket() process a hostname & port list; returns socket status
        process_url() process an URL list; returns each URL status
    """


    def __init__(self, list1, list2=None, username=None, password=None):
        self.list1 = list1
        self.list2 = list2
        self.username = username
        self.password = password

    def process_host(self):
        """Iterate over a hosts list and calls method check_host with host as
        argument.
        """
        for hostname in self.list1:
            print self.check_host(hostname)

    def process_socket(self):
        """Iterate over a host and port list and calls method check_socket and
        call method check_socket with a hostname and a port as arguments.
        """
        for hostname in self.list1:
            for port in self.list2:
                print self.check_socket(hostname, port)

    def process_url(self):
        """Iterate over a URL list and call method check_url with an URL as an
        argument."""
        for url in self.list1:
            print self.check_url(url)

    def process_ssh(self):
        """Iterate over a hosts and commands list and call method ssh with
        a hostname, command, username, and password as arguments.
         """
        for hostname in self.list1:
            for command in self.list2:
                print self.ssh(hostname, command, self.username, self.password)

    def check_host(self, name):
            """Ping a given hostname four times, and return network-related
            information such as packet loss and latency."""
            command = 'ping -c 4 -s 1450 ' + name
            proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            output = proc.communicate()
            match = re.search(r'---(.*)', output[0], re.DOTALL)

            try:
                return match.group()
            except AttributeError:
                return '\n!!!Unable to resolve %s; check its DNS!\n' % self.name

    def check_socket(self, name, port):
        """Check status of a given socket (hostname and Port)."""

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((name, port))
        except socket.error:
            return '!!!Unable to connect to %s on port %s.' % (name, port)
        else:
            return 'Port %s is open on %s.' % (port, name)
        finally:
            sock.close()

    def check_url(self, name):
        """Check the status of a given URL and returns its code."""

        try:
            connection = urllib2.urlopen(name)
            code = connection.getcode()
        except urllib2.HTTPError as e:
            return '!!!There is an http problem with %s. s%' % (name, e)
        except urllib2.URLError as e:
            return '!!!There is an URL problem with %s. s%' % (name, e)
        else:
            return 'URL %s returned a code of %s.' % (name, code)

    def ssh(self, node, command, username, password):
        paramiko.util.log_to_file('paramiko.log')
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(node, 22, username, password)
        except socket.error:
            return 'Node %s is not answering; check hostname or IP.' % node
        except paramiko.AuthenticationException:
            return 'Authentication failed; check username and password.'
        except KeyboardInterrupt:
            print '  Goodbye'
            exit()
        else:
            stdin, stdout, stderr = client.exec_command(command)
            print stdout.read()
        finally:
            client.close()