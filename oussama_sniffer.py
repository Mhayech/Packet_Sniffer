import urllib
import socket
import struct

def main():
    conn = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3))
    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print('Ethernet frame :')
        print(f'Destination: {dest_mac}, Source: {src_mac}, Protocol: {eth_proto}')
#Unpacking Ethernet Frame
def ethernet(data):
    dest_mac, src_mac, ptype = struct("! 6s6s2s",data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(ptype), data[14:]


# Formatting MAC address (MAke it Human Readable)
def get_mac_addr(byte_address):
    byte_str = map('{:02x}'.format,byte_address)
    mac_addr = ':'.join(byte_address).upper()
    return mac_addr
#Unpacking IPv4 Packet
def ip_packet(data):
    version_header = data[0]
    version = version_header >> 4
    header_len = (version_header & 15)*4
    time_to_live, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version_header, version, time_to_live,proto,target,src,data[header_len:]

def ip(addr):
    return '.'.join(map(str),addr)
main()
 