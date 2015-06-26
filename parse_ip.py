import re
import socket

def parse_ip(file_name):
    fp = open(file_name, 'r')
    text = fp.read()
    tuples = re.findall(r'((?:\d{1,3})\.(?:\d{1,3})\.(?:\d{1,3})\.(?:\d{1,3}))', text)
    output = []
    for ip_addr in tuples:
        try:
            socket.inet_aton(ip_addr)
            output.append(ip_addr)
        except socket.error:
            continue
    print output



parse_ip('ip.txt')
