
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
* Prints which IPs are **reachable (active)** and *ignore* which are not.

---

### 🧩 Example Use Case

\> [OPEN] - 192.168.1.14:80
\> [OPEN] - 192.168.1.14:80

---

## ▶️ Run the Script

```bash
python activeip.py
```

Or if arguments are supported:

```bash
python activeip.py 192.168.1.1 20 80
```
---
