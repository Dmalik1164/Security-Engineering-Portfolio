````
# Target VM Creation & Isolated Cyber Lab Setup

## Objective

Today’s project was to create a target virtual machine for cybersecurity home lab practice while ensuring the environment remained isolated from my home network and external infrastructure. Before starting, I planned the project around UK cybersecurity law and National Cyber Security Centre guidance to ensure the lab remained safe and ethical.

My goal was to create a vulnerable target machine that could later be used for:

* Nmap scanning
* vulnerability testing
* SIEM logging
* Elastic Stack and Kibana visualisation
* KQL query practice

I discussed my planned setup with AI beforehand to confirm that the architecture and isolation methods would remain within safe and legal boundaries.

---

## Virtual Machine Creation

To begin, I created a new virtual machine in Oracle VM VirtualBox using Metasploitable 2, an intentionally vulnerable Linux virtual machine designed for cybersecurity training. I allocated:

* 2GB RAM
* 1 CPU core

Since the machine would mainly function as a lightweight command-line target system rather than a graphical desktop environment, lower hardware allocation was sufficient.

Instead of manually creating storage, I attached the preconfigured Metasploitable virtual hard disk downloaded from SourceForge.

Once the target VM successfully booted, I shut down both the Kali attacker VM and the Metasploitable target VM to begin configuring an isolated network.

---

## Network Isolation

Using AI guidance, I changed both virtual machines from NAT networking to VirtualBox “Internal Network” mode and assigned them the same internal network name:

```
CyberLab
````

Changing from NAT to Internal Network removed internet access and prevented communication with external infrastructure. This created a closed virtual network existing only inside VirtualBox, allowing communication only between the connected virtual machines.

---

## IPv4 Configuration

After configuring the network, I checked both systems for valid IPv4 addresses using:

```
ifconfig
```

and:

```
ip a
```

Neither machine initially had a usable IPv4 address because the Internal Network did not provide DHCP services. To solve this, I manually configured both systems with static IPv4 addresses inside the same subnet.

### Kali Attacker VM

```
sudo ip addr add 192.168.56.10/24 dev eth0
sudo ip link set eth0 up
```

### Metasploitable Target VM

```
sudo ifconfig eth0 192.168.56.20 netmask 255.255.255.0 up
```

This placed both systems within the same subnet while remaining isolated from my real network.

---

## Troubleshooting

During testing, I encountered a:

```
Network is unreachable
```

error when attempting to ping the target machine from Kali.

To troubleshoot this, I first verified that the target machine retained its manually assigned IPv4 address correctly. After confirming the target VM was configured properly, I began investigating the Kali attacker VM instead.

I realised that although the `eth0` interface was active, Kali was not correctly retaining the manually assigned IPv4 configuration. Since the Kali VM had previously been connected using NAT networking, I suspected stale network configuration may have interfered with the new isolated setup.

Using AI guidance, I flushed the existing IP configuration from the Kali VM’s `eth0` interface using:

```
sudo ip addr flush dev eth0
```

After reassigning the IPv4 address and verifying the interface using:

```
ip a
```

the system successfully retained the correct address.

---

## Connectivity Validation

I then repeated the connectivity test and successfully established communication between the Kali attacker VM and the Metasploitable target VM using:

```
ping 192.168.56.20
```

This confirmed that the isolated internal cyber lab had been configured successfully.

---

## What I Learned

During this project I improved my understanding of:

* NAT vs Internal Network
* subnetting
* manual IPv4 assignment
* Linux network interfaces
* isolated lab architecture
* troubleshooting network configuration issues

Most importantly, I learned how important controlled isolation and careful network configuration are when creating cybersecurity practice environments.

```
```
