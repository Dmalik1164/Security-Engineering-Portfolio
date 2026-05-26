## Kali Lab Creation

### Aim
Create a dedicated Kali Linux virtual machine configured with outbound internet access. This setup establishes a personal penetration testing platform to perform TryHackMe and HackTheBox challenges using local tools and resources, rather than relying on the web-based attack machines provided by the platforms.

### What I Did
Prior to creating this lab, I had configured a Kali virtual machine several months ago. However, that machine was subsequently modified into a dedicated attack box within an isolated, host-only network environment alongside a Metasploitable target box to safely practice Nmap scans and exploit mechanics without risking public network infrastructure.

To build this new, internet-facing lab, I began by initializing a new virtual machine in VirtualBox. I assigned the system 4GB of RAM, 2 CPU cores, and a 25GB virtual hard disk. For the operating system profile, I selected Debian (64-bit) as the base template to match Kali's architecture.

For network architecture, I selected the NAT (Network Address Translation) adapter. This creates a secure, unidirectional communication channel where the virtual machine is masked behind the host laptop's network identity. It allows the VM to safely talk out to the public internet while remaining completely hidden from external inbound scans.

Once the installation was complete, I verified external network connectivity by sending an ICMP (Internet Control Message Protocol) echo request using the command:

---
ping -c 4 google.com
---

The virtual machine successfully transmitted 4 packets to Google's servers and received 4 replies with 0% packet loss, confirming active DNS resolution and external routing.

### What Went Well
My prior experience building virtual machines allowed me to navigate the initial configuration efficiently without step-by-step guidance. I successfully managed a host storage allocation issue mid-install, recovered the VM state, and finalized the GRUB bootloader setup cleanly.

### What I Could Improve On
Developing a more thorough, instinctive grasp of low-level system terminology—specifically regarding automated disk partitioning schemas—to increase independence and reduce hesitation during advanced Linux installation phases.
