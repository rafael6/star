star
====


A simple yet effective way to remotely test IT systems. 

The idea is to create a module (toolkit) containing the necessary resources to be able to test IT systems remotely.
Below is a list of the capabilities to this point:
1. Check DNS resolution.
2. Check IP reachability status.
3. Check services (socket) status. 
4. Check URL status.
5. Additionally, this module contains an additional class for telnet and SSH channel creation; 
and for command and command output handling.

Below is the module toolkit structure:
  Toolkit
    +check_host(hostname): tuple        stdout containing DNS resolution and ICMP details.
    +check_socket(hostname, port):      successful creation of a socket object
    +check_url(url): int                URL status code
  
  Connect
    +ssh(node, command, username, password):     successful creation of an SSH channel and command processing.
    +telnet(node, command, username, password)   successful creation of a telnet channel and command processing.
 
Supporting modules:
Module system1 is an example of a test construct for a particular IT system. This module represents the system in question and
it is a collection of applicable method calls. The resources from module toolkit are consumed at this level.

Module index is the start of the program and it is useful when creating two or more system constructs. 
  
Third party dependencies:
paramiko is the only third party library and it is used by the SSH method.
http://www.paramiko.org/en/latest/

OS support:
This module was written for any Linux distribution, but it also runs well in MacOS. For Windows support, 
only the regular expression that is part of the check_host method needs to be modified.
