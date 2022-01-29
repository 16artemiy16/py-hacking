# portscan
Scans opened ports on a given host.

## Usage

```shell
# Scan single port
python3 portscan.py google.com:80
# or
python3 portscan.py google.com 80

# Scan ports 1, 10, 11, 12, 13, 105
python3 portscan.py google.com 1 10-13 105
```
