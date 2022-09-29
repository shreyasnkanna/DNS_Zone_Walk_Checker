# DNS_Zone_Walk_Checker

### Author : Shreyas.N

This tool will check whether DNS Zone Walking is enabled or not for the given domain or not

This tool accepts single/list of domains as command line argument or pass list of domain through input file.

#### Python Requirements:
* argparse
* dns.resolver

#### Additional Requirements:
* dig tool (Linux)

#### Options Available:
```
usage: DNS_Zone_Walking.py [-h] [-i INPUT [INPUT ...]] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                        Enter Domain to check DNS Security Configs (seperated by space for multiple inputs)
  -f FILE, --file FILE  Enter full path to Input File

```

#### Tool Usage:
To pass single/list of domains as argument:

``` $ python3 DNS_Zone_Walking.py -i <Domain1> <Domain2>```

To pass list of domains inside the file:

``` $ python3 Domain_Rep_Check.py -f <Input File Path>```
