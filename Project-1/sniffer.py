import socket
import struct

# Map protocol numbers to human-readable names
PROTOCOL_MAP = {1: "ICMP", 6: "TCP", 17: "UDP"}

def parse_packet(packet):
    ip_header = packet[:20]  # Extract IP header
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

    src_ip = socket.inet_ntoa(iph[8])
    dst_ip = socket.inet_ntoa(iph[9])
    protocol = iph[6]
    
    protocol_name = PROTOCOL_MAP.get(protocol, "OTHER")
    
    print(f"[+] Packet: {src_ip} -> {dst_ip} | Protocol: {protocol_name} ({protocol})")

# Create a raw socket
try:
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    sniffer.bind(("0.0.0.0", 0))  # Bind to all interfaces
    
    # Include IP headers
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    print("[*] Starting network sniffer...")
    
    while True:
        packet, _ = sniffer.recvfrom(65565)  # Capture packets
        parse_packet(packet)

except PermissionError:
    print("[!] Run the script as root/admin (sudo).")

except KeyboardInterrupt:
    print("\n[*] Stopping sniffer...")
    sniffer.close()