import argparse
import re


def parse_args():
    parser = argparse.ArgumentParser(
        prog='portscan',
        description='Check open ports by host',
        epilog='Have a nice hacking! :)'
    )
    parser.add_argument('host', metavar='host', type=str, help='The host on which to check open ports')
    parser.add_argument(
        'ports',
        metavar='ports',
        type=str,
        help='One port, a list, or range divided by dash (inclusive, i.e. 2-5 == 2,3,4,5)',
        nargs=argparse.REMAINDER,
    )

    args = vars(parser.parse_args())

    host_and_port = args['host'].split(':')
    host = host_and_port[0]
    ports = []

    if len(host_and_port) == 2:
        ports.append(int(host_and_port[1]))

    for port in args['ports']:
        # Range of ports, i.e. 5-40 (INCLUSIVE)
        if re.match('\d+-\d+', port):
            left, right = port.split('-')
            ports.extend(range(int(left), int(right)+1))
        # One port
        else:
            ports.append(int(port))

    # Exclude repeatable ports
    ports = list(set(ports))

    return {'host': host, 'ports': ports}
