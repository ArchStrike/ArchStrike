#!/usr/bin/env python2
# dnsbf.py
# Written by t0ka7a
# Edited by strayArch
# License: new BSD Licence
# Purpose: find hostnames on subnetwork

import sys
from socket import gethostbyaddr


def main():
    intro()
    net = None
    # Check argument count
    if len(sys.argv) == 2:
        net = check_network_syntax(sys.argv[1])
    else:
        sys.stdout.write("Wrong number of arguments\n")
        sys.exit(0)
    for ip_to_test in net:
        hostname_check(ip_to_test)
    outro()

def intro():
    sys.stdout.write("[SEARCH INITIATED]\n")

def check_network_syntax(net):
    '''
    Note:
        struct can be used to convert ip's into int's as well.
    '''
    ip = None
    cidr = None
    try:
        ip, cidr = net.split('/')
        cidr = int(cidr)
        octet_generator = (int(octet) for octet in ip.split('.'))

        # Convert ip to int 
        bit = 24
        ip = 0
        for octet in octet_generator:
            # Check octet size 
            if octet > 0xFF or octet < 0x00:
                raise ValueError 
            else:
                ip  += octet << bit
                bit -= 8

        # Check cidr 
        if cidr > 32 or cidr < 0:
            raise ValueError
    except (ValueError, TypeError, SyntaxError) as e:
        print e
        sys.exit(1)

    mask_ip = 0
    for i in range(32 - cidr):
        mask_ip |= 1 << i

    # Create generator for IP's
    ip_generator = ( "%d.%d.%d.%d" % ( (i >> 24)&0xFF, (i >> 16)&0xFF, 
                                       (i >>  8)&0xFF, (i >>  0)&0xFF )\
                   for i in range(ip, min(ip + mask_ip + 1, 0xFFFFFFFF)) )
    return ip_generator

def hostname_check(ip):
    try:
        sys.stdout.write( "%s: %s\n" % (ip, gethostbyaddr(ip)[0]) )
    except:
        pass

def outro():
    sys.stdout.write("[SEARCH COMPLETED]\n")


if __name__ == "__main__":
    try:
        main()
    except:
        sys.exit(1)