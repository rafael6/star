star
====

A simple yet effective way to remotely test IT systems. 

The idea is to create a module (toolkit) containing the necessary resources to be able to test IT systems remotely.
Below is a list of the capabilities to this point:
1. Check DNS resolution including A-records, host records, c-names, and MX records
2. Check IP reachability status.
3. Check services (socket) status. 
4. Check URL status.

Supporting modules:
Module toolkit is the core of the program and contains methods for each capability.
Module element is the interface for a particular system or application construct.
Module system1 is a simple model or template for a particular system or application.
Module index is the start of the program and it is useful when creating a collection of systems or applications.
  
External modules:
import dns.resolver
import socket
import subprocess
import urllib.request

OS support:
This module was written for any Linux distribution, but it also runs well in MacOS.
Only minor changes are needed to work on Windows OS.
