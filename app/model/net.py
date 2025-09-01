import random
import ipaddress

def get_random_ipv4(n: int):
    arr = [str(ipaddress.IPv4Address(random.getrandbits(32))) for _ in range(n)]
    return arr

def get_random_ipv6(n: int):
    arr = [str(ipaddress.IPv6Address(random.getrandbits(128))) for _ in range(n)]
    return arr
    