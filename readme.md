
## 🔍 Open Port / Active IP Checker

A simple Python utility to **scan IP addresses and check whether a specific port is active or not**.

This tool is useful for:

* Checking active devices in a local network
* Verifying if a service is running on a given port
* Basic network diagnostics

---
### 📌 Purpose

If you are working with a local device and its IP address is not fixed, this tool helps you identify which ports are exposed by iterating through possible IPs.

### 🚀 How It Works

* Takes a **base IP address**
* Iterates over a range of IPs (e.g. `.1` to `.20`)
* Tries to connect to a given **port**
* Prints which IPs are **reachable (active)** and which are not

---

### 🧩 Example Use Case

```text
[CLOSED] 192.168.1.5:9090
[CLOSED] 192.168.1.6:9090
[CLOSED] 192.168.1.7:9090
[CLOSED] 192.168.1.8:9090
[CLOSED] 192.168.1.9:9090
[CLOSED] 192.168.1.10:9090
[CLOSED] 192.168.1.11:9090
[CLOSED] 192.168.1.12:9090
[CLOSED] 192.168.1.13:9090
> [OPEN] 192.168.1.14:9090
[CLOSED] 192.168.1.15:9090
[CLOSED] 192.168.1.16:9090
[CLOSED] 192.168.1.17:9090
```
---

## ▶️ Run the Script

```bash
python open_port_checker.py
```

Or if arguments are supported:

```bash
python open_port_checker.py 192.168.1 20 9090
```

---



---
