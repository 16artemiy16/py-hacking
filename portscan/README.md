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

# Log ports only after all are scanned: 
# --log-bunch (-lb), the opposite is --log-straight (-ls)
python3 portscan.py -lb google.com 78-81

# Log only opened ports: 
# --only-opened (-oo), the opposite is --only-closed (-oc)
python3 portscan.py -oo google.com 78-81
```
