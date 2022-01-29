import socket


def scan_port(addr, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((addr, port))

    if result == 0:
        print(f'[+] {port} is open')
    else:
        print(f'[-] {port} closed')
    sock.close()


def scan_ports(host, ports):
    addr = socket.gethostbyname(host)
    socket.setdefaulttimeout(1)

    for port in ports:
        scan_port(addr, port)
