
class pyIDS_info(object):

    def get_mac_gateway(ip_address):
        response, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address), \
        timeout = 2, retry = 2)

    
