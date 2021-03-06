import socket
import threading

from progressbar import Progressbar


def scan_port(addr, port, config):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((addr, port))

    is_opened = None

    if result == 0:
        if config['log_v_opened'] and config['log_t_straight']:
            print(f'[+] {port} is open')
        is_opened = True
    else:
        if config['log_v_closed'] and config['log_t_straight']:
            print(f'[-] {port} closed')
        is_opened = False

    sock.close()

    return is_opened


def scan_ports(host, ports, config):
    if config['log_t_bunch']:
        progress = Progressbar(len(ports))

    addr = socket.gethostbyname(host)
    socket.setdefaulttimeout(1)

    threads = []

    opened_ports = []
    closed_ports = []

    lock = threading.Lock()

    def scanning_thread(port):
        is_opened = scan_port(addr, port, config)

        lock.acquire()

        if is_opened:
            opened_ports.append(port)
        else:
            closed_ports.append(port)

        if config['log_t_bunch']:
            progress.next()

        lock.release()

    for port in ports:
        t = threading.Thread(target=scanning_thread, args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    if config['log_t_bunch']:
        if config['log_v_opened']:
            print('Opened', opened_ports)
        if config['log_v_closed']:
            print('Closed', closed_ports)
