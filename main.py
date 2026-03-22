import socket
import argparse

is_package = True

def is_port_open(ip, port, timeout=0.001):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((ip, port)) == 0
    except Exception:
        return False


def scan_ip_range(base_ip: str, start: int, count: int, port: int, show_all: bool):
    base_parts = base_ip.split(".")[:-1]
    base = ".".join(base_parts)

    for i in range(start, start + count):
        ip = f"{base}.{i}"
        if is_port_open(ip, port):
            print(f"-> [OPEN] {ip}:{port}")
        else:
            if show_all:
                print(f"[CLOSE] {ip}:{port}")
    input("Press any key to exit...")

if __name__ == "__main__":
    if is_package:
        base_ip = input("Enter Base ip (192.168.1.0): ") or "192.168.1.0"
        print("Specify the Range of IP lookup")
        start = input("Start IP number (default: 1): ") or "1"
        count = input("How many IPs to scan (default: 20): ") or "20"
        port = input("Port to check (default: 80): ") or "80"
        show_all = input("Show open Port only (default: y) y/n: ") or "y"
        show_all = show_all != "y"
        scan_ip_range(base_ip, int(start), int(count), int(port), show_all)
    else:
        parser = argparse.ArgumentParser(description="Scan IP range for open port")
        parser.add_argument( "base_ip", nargs="?", default="192.168.1.0", help="Base IP (default: 192.168.1.0)" )
        parser.add_argument( "start", nargs="?", type=int, default=1, help="Start IP number (default: 1)" )
        parser.add_argument( "count", nargs="?", type=int, default=20, help="How many IPs to scan (default: 20)" )
        parser.add_argument( "port", nargs="?", type=int, default=80, help="Port to check (default: 80)" )
        args = parser.parse_args()
        scan_ip_range( args.base_ip, args.start, args.count, args.port)
