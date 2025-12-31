import socket
import argparse

def is_port_open(ip, port, timeout=0.001):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((ip, port)) == 0
    except Exception:
        return False


def scan_ip_range(base_ip, start, count, port):
    base_parts = base_ip.split(".")[:-1]
    base = ".".join(base_parts)

    for i in range(start, start + count):
        ip = f"{base}.{i}"
        if is_port_open(ip, port):
            print(f"-> [OPEN] {ip}:{port}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan IP range for open port")

    parser.add_argument( "base_ip", nargs="?", default="192.168.1.0", help="Base IP (default: 192.168.1.0)" )
    parser.add_argument( "start", nargs="?", type=int, default=1, help="Start IP number (default: 1)" )
    parser.add_argument( "count", nargs="?", type=int, default=20, help="How many IPs to scan (default: 20)" )
    parser.add_argument( "port", nargs="?", type=int, default=80, help="Port to check (default: 80)" )
    args = parser.parse_args()

    scan_ip_range( args.base_ip, args.start, args.count, args.port)
