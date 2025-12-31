import socket

def is_port_open(ip, port, timeout=1):
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
            print(f"[OPEN  ] {ip}:{port}")
        else:
            print(f"[CLOSED] {ip}:{port}")


if __name__ == "__main__":
    BASE_IP = "192.168.1.0"
    START_IP = 1
    COUNT = 20
    PORT = 9090

    scan_ip_range(BASE_IP, START_IP, COUNT, PORT)
