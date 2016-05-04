star
====

A simple yet effective way to remotely test IT systems. 

The idea is to create a module (toolkit) containing the necessary resources to be able to test IT systems remotely.
Below is a list of the capabilities to this point:
1. Check DNS resolution including A-records, host records, c-names, and MX records
2. Check IP reachability status.
3. Check services (socket) status. 
4. Check URL status.

Modules:
toolkit: the core of the program and contains methods for each of the four tools (capabilities). Module toolkit
cosumes the following external modules:
  dns.resolver
  socket
  subprocess
  urllib.request

element: The interface for a particular system or application construct. Module element comsumes module toolkit.

SDcripts:
system1: A simple sample or template for a particular system or application. Script system1 comsumes module
element.
index: The start of the program and it is useful when creating a collection of systems to be tested and documented. 
  


OS support:
This module was written for any Linux distribution, but it also runs well in MacOS.
Only minor changes are needed to work on Windows OS.
