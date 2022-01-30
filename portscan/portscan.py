import parser
import scanner


if __name__ == '__main__':
    data = parser.parse_args()
    scanner.scan_ports(data['host'], data['ports'], data)
