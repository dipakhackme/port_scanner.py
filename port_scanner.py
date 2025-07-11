import socket

def scan_ports(ip):
    for port in range(1, 1025):
        sock = socket.socket()
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} open")
        sock.close()

ip = input("Enter IP to scan: ")
scan_ports(ip)
