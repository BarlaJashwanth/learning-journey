
# What is Nmap?

**Nmap** is short for **Network Mapper**. It is an open-source Linux command-line tool used to scan IP addresses and ports in a network and to detect installed applications.

---

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

  * 1]  code: nmap targeted ip
  * example: nmap 192.168.230.45

  what it does : it scans top 1000 common TCP ports (to be noted not 1000 ports 1 to 1000, it scans common tcp top 1000 ports )

  <img width="313" height="248" alt="image" src="https://github.com/user-attachments/assets/babe2197-3292-44d2-b0d9-a428f796b133" />
  

  * 2]  code: nmap -sU -sT targeted ip
  * example: nmap -sU -sT 192.168.230.45
 
    what it does : it scans top 1000 common UDP and TCP ports (to be noted not 1000 ports 1 to 1000, it scans common udp 1000 ports) it took 1000 seconds approx
    -sU stands for UDP
    -sT stands for TCP

    <img width="327" height="320" alt="image" src="https://github.com/user-attachments/assets/5d108265-979a-4c56-82f3-e490b407b4cb" />
<img width="388" height="341" alt="image" src="https://github.com/user-attachments/assets/490325f0-f985-4851-8ae8-1265696219ac" />

* 3] code: nmap -sU targeted ip
* example: nmap -sU 92.168.230.45

 what it does : it scans top 1000 ports (common one)

 <img width="406" height="218" alt="image" src="https://github.com/user-attachments/assets/f8f58645-7e25-407e-9afd-96bf7adf1dd5" />

 4] nmap -p- targeted ip
   * example: nmap -p- 198.167.89.90
   * what does it do : scan all tcp ports
<img width="400" height="351" alt="image" src="https://github.com/user-attachments/assets/62ec5b66-24ca-4a44-87a7-53e78c78290d" />
<img width="376" height="215" alt="image" src="https://github.com/user-attachments/assets/76375920-222e-4c1f-9bf2-10ad08488ce4" />



 * example: nmap -sU -sT -p- 198.167.89.90
 * what does it do : scan all 65036 ports all TCP and UDP (sometimes firewall may block us)
 * takes huge time ...

 # TCP Headers Made Simple

TCP flags are short control signals that help two computers talk to each other reliably over a network.

## The 6 Control Flags

* **SYN (Synchronize)**: **"Hey, can we talk?"**  
  Starts a brand-new connection request.

* **ACK (Acknowledge)**: **"Got it!"**  
  Confirms that data was received successfully.

* **PSH (Push)**: **"Pass this along right now!"**  
  Tells the computer to deliver the data immediately without waiting for the buffer to fill up.

* **URG (Urgent)**: **"Read this first!"**  
  Marks high-priority data that must jump to the front of the line.

* **FIN (Finish)**: **"I'm all done, goodbye!"**  
  Gracefully ends an active connection.

* **RST (Reset)**: **"Hang up immediately!"**  
  Abruptly cancels a connection due to an error or a closed port.

---

## TCP headers

| Flag | Meaning | Plain English Role |
| :--- | :--- | :--- |
| **SYN** | Start Connection | Asks to open a new conversation. |
| **ACK** | Confirm Data | Says "I received your last message." |
| **PSH** | Bypass Buffer | Delivers live data (like chat text) instantly. |
| **URG** | High Priority | Processes emergency data before everything else. |
| **FIN** | Close Gracefully | Says "No more data to send, let's close." |
| **RST** | Abort Connection | Forces an instant shutdown when an error occurs. |

> **Security Note:** A packet marked with both `SYN` (Hello) and `FIN` (Goodbye) is invalid and usually indicates a hacker port-scanning attempt.

 ## 3 Way Handshake
 <img width="746" height="329" alt="image" src="https://github.com/user-attachments/assets/5ea5e0af-907f-4984-ae28-ed05ab142688" />

 3 way handshake is very much necessary for TCP connection UDP connection has no 3 way handshake 

 # TCP 3-Way Handshake Made Simple

The 3-way handshake is the 3-step process two computers use to start a reliable conversation over a network.

---

## The 3 Steps

1. **Step 1: SYN** — *"Can we talk?"*
   * Computer A sends a `SYN` packet to ask Computer B if it is open to starting a conversation.

2. **Step 2: SYN-ACK** — *"Yes! Can you hear me?"*
   * Computer B receives the request, agrees (`ACK`), and asks Computer A if it can hear them back (`SYN`).

3. **Step 3: ACK** — *"Yes, connection established!"*
   * Computer A sends a final `ACK` to confirm it received the response. The connection is now active, and data transfer can begin.

---

## Handshake Summary

| Step | Flag Sent | Plain English Meaning | Action |
| :--- | :--- | :--- | :--- |
| **1** | **SYN** | "Hey, are you free to chat?" | Sender initiates connection |
| **2** | **SYN + ACK** | "Yes I am! Can you hear me?" | Receiver confirms and responds |
| **3** | **ACK** | "Got it! Let's start." | Sender confirms; connection open |

> **Real-World Analogy**: Think of it like a phone call.  
> You say **"Hello?"** (SYN) -> They reply **"Hi! Can you hear me?"** (SYN-ACK) -> You say **"Yep, loud and clear!"** (ACK). Now you start talking.


## Closed Port (Connection Refused)

The target computer receives your request, but no program is listening on that port.

* **Step 1:** Computer A sends **SYN** (*"Hey, can we talk on Port 80?"*).
* **Step 2:** Computer B replies with **RST-ACK** (*"No! Nobody is here, go away!"*).
* **Result:** The connection attempt is instantly rejected.

  ## 5] nmap -sn targeted ip : this tells wheather ip address is up or down
  <img width="409" height="99" alt="image" src="https://github.com/user-attachments/assets/8502198e-1ea7-41df-a289-3010c7e27062" />
  <img width="503" height="71" alt="image" src="https://github.com/user-attachments/assets/3ce5f7fb-8096-44b4-a795-9813722abd14" />
  * in both cases above metasplot kept open in first case and in second case metasploit is closed so ipadress is up and down in two differnt cases


<img width="813" height="235" alt="image" src="https://github.com/user-attachments/assets/83f14b06-10bd-4f15-acf1-dec4a3531d94" />
* in this above case at a time we are scanning 100 IP adresses at a time
  
* my metasploit ip : 192.168.230.129
* my kali linux ip : 192.168.230.128
<img width="430" height="157" alt="image" src="https://github.com/user-attachments/assets/77143547-5edb-4edd-9f6c-f23952f1aa7f" />


## 6] sudo netdiscover -i eth0
<img width="491" height="108" alt="image" src="https://github.com/user-attachments/assets/d67a0266-0a7a-4d5d-9163-aa79eaff1056" />
* this gives who all conected to network

## 7] nmap -sn -iL file name 
<img width="266" height="155" alt="image" src="https://github.com/user-attachments/assets/d56e6a78-9eff-4bef-b348-d8f46e103708" />
<img width="182" height="102" alt="image" src="https://github.com/user-attachments/assets/4e720ca3-34df-4ae8-9536-2cb2dd6ac72e" />
* saving it on desktop and just dragging it and pasting at file name which contains valid ip it just analyse and tell weather host is up or down
<img width="381" height="122" alt="image" src="https://github.com/user-attachments/assets/1620d906-5d3c-4c67-9add-b0602e41afc5" />










    
    

