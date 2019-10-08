#!/usr/bin/env python3

import argparse
import os
import random
#from scapy.all import *

aport = 0
bport = 0
singleport = 0
src = "0.0.0.0"

#parse inputted range. Valid inputs= a-, -b, a-b, a
def rparse(r):
    global aport
    global bport
    global singleport
    #if not singleport
    if "-" in r:
        a = r.split("-")[0].strip()
        b = r.split("-")[1].strip()
        #check if in -b format
        if not a:
            aport = 0
            #check if b is valid number
            if b.isnumeric() and 0<=int(b)<=65535:
                bport = int(b)
                return(aport,bport)
            else:
                return("Make sure to have correct format")
        #check if in a- format
        elif not b:
            bport = 65535
            #check if a is valid number
            if a.isnumeric() and 0<=int(a)<=65535:
                aport = int(a)
                return(aport,bport)
            else:
                return("Make sure to have correct format")
        #must be in a-b format. check if valid
        if a.strip().isnumeric() and 0<=int(b)<=65535 and int(a)<int(b) and 0<=int(b)<=65535 and b.strip().isnumeric():
            aport = a
            bport = b
            return(aport,bport)
        else:
            return("Make sure to have correct format")
    #if singleport
    elif r.strip().isnumeric() and 0<=int(r)<=65535:
        singleport = int(r)
        return(singleport)
    else:
        return("Make sure to have correct format")

#parse inputted spoofed src ip address. only valid input = xxx.xxx.xxx.xxx; xxx is between 0-255
def srcparse(src):
    a,b,c,d = [src.split(".")[i].strip() for i in range(4)]
    #check if any quad is an empty string
    if not a or not b or not c or not d:
        return("Make sure to have correct format")
    #check if all quads are numeric
    if a.isnumeric() and b.isnumeric() and c.isnumeric() and d.isnumeric():
        #check if all in valid range
        if 0<=int(a)<=255 and 0<=int(b)<=255 and 0<=int(c)<=255 and 0<=int(d)<=255:
            src = "{}.{}.{}.{}".format(a,b,c,d)
            return("valid")
        else:
            return("Make sure to have correct format")
    else:
        return("Make sure to have correct format")

#psuedo-randomly generated MAC address
def randmac():
    # should be in octet format AA:BB:CC:DD:EE:FF
    mac = ""
    add = [random.choice("0123456789ABCDEF") for _ in range(12)]
    for i in range(len(add)):
        mac = mac + add[i]
        if i%2==1 and i!=len(add)-1:
            mac = mac + ":"
    return (mac)

#psuedo-randomly generated IPv4 address
def randipv4():
    ip = ""
    quad = [random.choice(range(255)) for _ in range(4)]
    for i in range(len(quad)):
        if i == 3:
            ip = ip + str(quad[i])
            return(ip)
        ip = ip + str(quad[i]) + "."

#psuedo-randomly generated IPv6 address
def randipv6():
    ip = ""
    octet = [hex(random.randint(0,65535))[2:] for _ in range(8)]
    for i in range(len(octet)):
        if i == len(octet)-1:
            ip = ip + str(octet[i])
            return(ip)
        ip = ip + str(octet[i])+":"
        if random.choice(range(5))==3 and i>1:
            ip = ip[:-1]
            ip = ip[:-(len(ip)-ip.rindex(":"))] + ":0:"





parser = argparse.ArgumentParser()
parser.add_argument("dest",help="Destination IP address;quad-dotted notation")
parser.add_argument("-r","--range",help="port range",nargs="?",default="0-65535",metavar="range")
parser.add_argument("-s","--source",help="spoof source IP address;quad-dotted notation")
parser.add_argument("-t","--tcp",help="tcp scan",action="store_true")
parser.add_argument("-x","--stealth",help="stealth tcp scan",action="store_true")
args = parser.parse_args()

print(randmac())
print(randipv4())
print(randipv6())