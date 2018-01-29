import socket
import fcntl
import struct
import array

class idsInfo(object):
    def all_interfaces():
        maxInt = 128
        byte = maxInt *32
        s = socket.socket(socket.AF_INET, socket.SOCKDGRAM)
        
    def get_mac_gateway(ip_address):
        response, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address), \
        timeout = 2, retry = 2)
