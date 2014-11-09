#!/usr/bin/python

__author__ = 'Rafael'

import paramiko
import re
import socket
import subprocess
import telnetlib
import urllib2


class Toolkit(object):
    """
    Provides the following methods:
        check_host() for DNS resolution and ICMP stats.
        check_socket() for socket/service status checking.
        check_url() for URL status code checking.
    """

    def __init__(self, name, port=None, username=None, password=None):
        self.name = name
        self.port = port
        self.username = username
        self.password = password

    def check_host(self):
        """Ping a given hostname (argument) with a load of 1450 data bytes four
        times and returns DNS resolution and ICMP-related information such as
        packet and latency counters."""
        command = 'ping -c 4 -s 1450 ' + self.name
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output = proc.communicate()
        match = re.search(r'---(.*)', output[0], re.DOTALL)

        try:
            return match.group()
        except AttributeError:
            return '\n!!!Unable to resolve %s; check its DNS!\n' % self.name

    def check_socket(self):
        """Check status of a given socket (hostname and port) (arguments) and
        returns its connectivity status."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((self.name, self.port))
        except socket.error:
            return '!!!Unable to connect to %s on port %s.' % (self.name, self.port)
        else:
            return 'Port %s is open on %s.' % (self.port, self.name)
        finally:
            sock.close()

    def check_url(self):
        """Check the status of a given URL (argument) and returns its URL
        status code."""
        try:
            connection = urllib2.urlopen(self.name)
            code = connection.getcode()
        except urllib2.HTTPError as e:
            return '!!!There is an http problem with %s. s%' % (self.name, e)
        except urllib2.URLError as e:
            return '!!!There is an URL problem with %s. s%' % (self.name, e)
        except Exception as e:
            return e
        else:
            return 'URL %s returned a code of %s.' % (self.name, code)


class Connect():
    """
    Provides the following methods:
        ssh() open an ssh channel with a given node and command processing.
        telnet() open a telnet chanel with a given host and process commands.
    """

    def __init__(self, node, commands, username=None, password=None):
        self.node = node
        self.commands = commands
        self.username = username
        self.password = password

    def ssh(self):
        """Open an SSH channel with a given node (IP or hostname) and process
        command(s) and its output. Takes a node, username, password, and a list
        object containing the command(s)."""
        paramiko.util.log_to_file('paramiko.log')
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(self.node, 22, self.username, self.password)
        except socket.error:
            return 'Node %s is not answering; check hostname or IP.' % self.node
        except paramiko.AuthenticationException:
            return 'Authentication failed; check username and password.'
        except KeyboardInterrupt:
            print '  Goodbye'
            exit()
        else:
            for command in self.commands:
                stdin, stdout, stderr = client.exec_command(command)
                print stdout.read()
        finally:
            client.close()

    def telnet(self):
        """Open a telnet channel with a given node (IP or hostname) and process
        command(s) and its output. Takes a node, username, password, and a list
        object containing the command(s)."""

        try:
            tn = telnetlib.Telnet(self.node)
            tn.read_until('login: ')
            tn.write(self.username + '\n')
            tn.read_until('Password: ')
            tn.write(self.password + '\n')
        except socket.error as e:
            print 'Unable to connect to %s. %s' % (self.node, e)
        except EOFError as e:
            print 'Connection closed and no data from %s. %s' % (self.node, e)
        except KeyboardInterrupt:
            print '  Goodbye'
            exit()
        else:
            for command in self.commands:
                tn.write(command + '\n')
                return tn.read_all()
        finally:
            tn.close()
