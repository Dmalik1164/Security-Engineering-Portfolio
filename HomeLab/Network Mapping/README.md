# Target Box Port Scan Practice

*(This project was completed inside a closed and isolated home lab environment in compliance with UK cybersecurity law and National Cyber Security Centre guidance.)*

## Project Aim

The aim of this project was to practice using Nmap while gradually building a better understanding of:

* what the commands are actually doing
* how network scanning works
* what information can be gathered from a target system
* how enumeration contributes to both offensive and defensive cybersecurity

---

## Key Notes

### Nmap

Nmap stands for **Network Mapper**. It is a network discovery, enumeration and port scanning tool used to:

* identify hosts
* discover open ports
* identify running services
* detect software versions
* map networks

---

### `-sV` (Service Version Detection)

Using:

```
-sV
```

enables Service Version Detection.

Without `-sV`, Nmap performs more basic service identification. With `-sV`, Nmap probes deeper into exposed services and attempts to identify:

* exact software
* version numbers
* banners
* server information

This is important because outdated software versions may contain known vulnerabilities.

---

## Important Nmap Flags

| Flag  | Purpose                    |
| ----- | -------------------------- |
| `-sV` | Service version detection  |
| `-sS` | SYN stealth scan           |
| `-O`  | Operating system detection |
| `-A`  | Aggressive scan            |
| `-p-` | Scan all ports             |
| `-Pn` | Skip host discovery        |

---

## What I Did

Before beginning the scan, I manually configured the IPv4 addresses on both the attacker VM and target VM. This was necessary because the IP configuration used in the isolated lab environment was temporary and reset after reboot.

### Attack Box (Kali)

```
sudo ip addr add 192.168.56.10/24 dev eth0
sudo ip link set eth0 up
```

### Target Box (Metasploitable)

```
sudo ifconfig eth0 192.168.56.20 netmask 255.255.255.0 up
```

After configuring both systems, I ran the following scan from the Kali attacker VM:

```
nmap -sV 192.168.56.20
```

The scan identified multiple open ports and active network services listening for communication.

Example result:

```
22/tcp open ssh OpenSSH 4.7p1 Debian
```

### Breaking Down the Result

| Section         | Meaning                   |
| --------------- | ------------------------- |
| `22`            | Port number               |
| `tcp`           | Network protocol          |
| `open`          | Port state                |
| `ssh`           | Service name              |
| `OpenSSH 4.7p1` | Detected software/version |

---

## Understanding Port States

### Open

An open port means a service is actively listening and accepting network communication.

### Closed

A closed port means no active service is listening on that port.

### Filtered

A filtered port usually means traffic is being blocked or filtered by a firewall or network filtering system.

---

## Services Identified During the Scan

The scan identified several exposed services including:

* FTP (File Transfer Protocol)
* Telnet (an older insecure remote access protocol)
* HTTP (web server service)
* SMB/Samba (Windows-style file and network sharing protocols)

Metasploitable is intentionally designed to be vulnerable and expose multiple services for cybersecurity training purposes. By scanning the target box, I improved my understanding of:

* attack surface analysis
* exposed services
* enumeration
* service identification
* vulnerability awareness

---

## Comparing Nmap With and Without `-sV`

I also ran:

```
nmap 192.168.56.20
```

without the `-sV` flag.

This produced a simpler result which identified open ports and basic service names, but it did not provide:

* exact software versions
* detailed banner information
* deeper service identification

This showed me why service version detection is important during both vulnerability assessment and defensive auditing. Older or exposed software versions may contain vulnerabilities and increase risk exposure.

I also learned that attackers may sometimes prefer lighter or quieter scans to reduce detection, while deeper scans such as `-sV` generate more traffic and are more likely to create logs or trigger security monitoring systems.

---

## What I Learned

During this project I improved my understanding of:

* network enumeration
* attack surface analysis
* open ports and exposed services
* Nmap scanning methodology
* service version detection
* why outdated services can increase security risk
* the relationship between reconnaissance and defensive monitoring

I also began developing a better understanding of how tools like Nmap are used in both offensive and defensive cybersecurity environments.
