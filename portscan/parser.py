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

    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument('-oo','--only-opened',help='Log only opened ports', action='store_true')
    verbosity_group.add_argument('-oc', '--only-closed',help='Log only closed ports', action='store_true')

    log_time_group = parser.add_mutually_exclusive_group()
    log_time_group.add_argument('-ls', '--log-straight', help='Log the port straight after it is scanned', action='store_true')
    log_time_group.add_argument('-lb', '--log-bunch', help='Log all ports at once after all are scanned', action='store_true')

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

    log_all_ports = not args['only_opened'] and not args['only_closed']

    return {
        'host': host,
        'ports': ports,
        'log_v_opened': args['only_opened'] or log_all_ports,
        'log_v_closed': args['only_closed'] or log_all_ports,
        'log_t_straight': not args['log_bunch'],
        'log_t_bunch': args['log_bunch'],
    }
