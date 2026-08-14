
# What is Nmap?

**Nmap** is short for **Network Mapper**. It is an open-source Linux command-line tool used to scan IP addresses and ports in a network and to detect installed applications.

---o

## Key Functions

* **Network Discovery:** Allows network admins to find which devices are running on their network.
* **Port & Service Detection:** Helps discover open ports and services.
* **Security Assessment:** Detects vulnerabilities on target systems.


## Background & Fun Facts

* **Creator:** Written by Gordon Lyon (pseudonym *Fyodor*) as a tool to map entire networks easily and find open ports and services.
* **Pop Culture:** Featured in movies like *The Matrix* and the popular series *Mr. Robot*.


# Why Use Nmap?

Nmap (Network Mapper) is a widely preferred tool among cybersecurity professionals for network scanning and security auditing. It allows users to quickly map out networks without needing complex commands, while offering flexibility for both basic checks and advanced scripting.

---

## Key Advantages

* **Simple & Advanced Operations:** Supports basic commands (e.g., checking if a host is active) up to complex automated scripts.
* **Network Device Discovery:** Quickly identifies all connected devices (servers, routers, switches, mobile devices, etc.) across single or multiple networks.
* **Service & Application Detection:** Identifies running services (web servers, DNS servers) and detects application versions to help find known vulnerabilities.
* **Operating System (OS) Fingerprinting:** Detects the OS type and version on target devices to aid in planning penetration testing strategies.
* **Vulnerability & Attack Testing:** Uses pre-written scripts from the Nmap Scripting Engine (NSE) during security audits to test systems for vulnerabilities.
* **Graphical Interface (Zenmap):** Includes a GUI called Zenmap that creates visual network maps for better usability and reporting.



  # What is a Port Scan?

A **port scan** is a technique used to discover open doors or weak points in a network. By sending messages to specific ports on a system and analyzing the responses, users can determine if ports are open, active, or protected.

---

## Purpose & Uses

* **Attacker Perspective:** Cybercriminals use port scans to find open ports, track data flow, test for weak points, and identify active security devices like firewalls.
* **Defender Perspective:** Businesses use port scanning to audit their own systems for vulnerabilities and ensure network security using tools like **IP scanning**, **Network Mapper (Nmap)**, and **Netcat**.

---

## Information Revealed by Port Scanning

* **Services running** on the system
* **Users** who own these services
* Whether **anonymous logins** are allowed
* Which network services **require authentication**

  ## Scanning TCP and UDP ports by using nmap:

  * code: nmap targeted ip
  * example: nmap 192.168.230.45

  what it does :
