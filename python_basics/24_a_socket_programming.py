### Basics of Networking :
"""

1. What is an IP Address?
IP (Internet Protocol) Address = Unique address of a device on a network.

Like a house address, it tells data where to go.
Every device on the same network must have a unique IP.

Example:
Laptop → 192.168.1.5
Phone  → 192.168.1.6
TV     → 192.168.1.7

2. Main Functions of an IP Address
Identifies a device on a network.
helps data travel (routing) from one device to another.

3. IPv4
Example: 192.168.1.10

Has 4 numbers separated by dots.
Each number is called an octet.
Each octet ranges from 0 to 255.

Valid:
192.168.1.5
10.0.0.1
8.8.8.8

Invalid:
192.168.500.1

4. Dot Decimal Notation

IPv4 is written as:
x.x.x.x

Example:
203.0.113.12

5. Static IP
Manually assigned.
Usually never changes.
Used for:
Servers
Printers
CCTV
Network devices
Example:
192.168.1.50

6. Dynamic IP
Automatically assigned by the router.
Can change when reconnecting.
Uses DHCP.

7. DHCP
DHCP = Dynamic Host Configuration Protocol
Simple meaning:
> Automatically gives IP addresses to devices.

Example:
Phone joins Wi-Fi
↓
Router gives
192.168.1.12

8. Private IP Address Ranges

Used inside local networks.
10.0.0.0 – 10.255.255.255
172.16.0.0 – 172.31.255.255
192.168.0.0 – 192.168.255.255

Commonly seen at home:
192.168.1.x

9. Public IP
Given by the ISP.
Visible on the Internet.
Used to communicate with the outside world.

Example:
49.207.xxx.xxx

10. Private vs Public IP
Private IP
Inside home/office/college network.
Cannot normally be reached directly from the Internet.

Public IP
Used on the Internet.
Given by the ISP.
Represents the entire network to the outside world.

11. IANA
IANA = Internet Assigned Numbers Authority
Simple meaning:
Organization that manages IP address ranges.
Defines the private IP ranges.

12. NAT (Network Address Translation)
Simple meaning:
> Many private devices share one public IP.
Example:
Laptop
192.168.1.3

Phone
192.168.1.4
      ↓
Router (NAT)
      ↓
Public IP
49.207.110.25
      ↓
Internet

Websites only see:
49.207.110.25
They do not see:
196.168.1.3

13. Why NAT is Needed

Without NAT:
Every device would need its own public IP.
With NAT:
50 Devices
↓
1 Public IP
This saves public IPv4 addresses.

14. Can I Scan a Friend's Public IP?
Yes, you can try to connect to the public IP.

However:
The connection first reaches the router.
The router decides whether to allow or block it.
Most home routers block unsolicited incoming connections by default.

So:
❌ Public IP ≠ Access to every device inside the network.


15. Port Forwarding (Basic Idea)
If the router is configured like this:
49.207.xxx.xxx:8080
↓
Router
↓
192.168.1.3:80
Then connections to the public IP on port 8080 are forwarded to the laptop.
Without such a rule, incoming connections are usually blocked.

16. Important Commands

Windows:
ipconfig /all

Shows:
IPv4 Address
Subnet Mask
Default Gateway
"""
"""
Packets

Packet is a small unit of data transmitted over a network.
Every packet has two parts:
Header
Payload

Header contains:
Source IP Address
Destination IP Address
Source Port
Destination Port
Protocol (TCP/UDP)
Control information

Payload contains the actual data (message, file, image, webpage, etc.).

Routers read the header to forward packets.
Different protocols (TCP, IP, Ethernet) add their own headers (encapsulation).
Python's socket module and the operating system create these headers automatically.


DNS (Domain Name System)
DNS stands for Domain Name System.
DNS converts domain names into IP addresses.
DNS is called the Internet's Phone Book.
It stores the mapping between hostnames (domain names) and IP addresses.
Users remember domain names; computers communicate using IP addresses.

Example:
google.com → IP Address
Network Scanner can accept a domain name or an IP address.
If a domain name is entered, DNS resolves it to an IP address before scanning.
"""
"""
PORTS

1. What is a Port?
A Port is a logical endpoint (door) through which a service communicates.
It tells the operating system which application should receive the data.

Analogy:
IP Address = Building Address 🏢
Port = Door/Room 🚪

2. Why are Ports Needed?
One computer runs many applications.
Ports help identify which application the incoming data belongs to.
Without ports, the operating system wouldn't know where to send the received data.

3. Total Number of Ports
Ports are 16-bit numbers.
Port Range = 0 – 65535
Total Ports = 65,536

4. Port Categories
A) Well-Known Ports (0–1023)
Used by common services.
Most important ports to remember:
22 → SSH
53 → DNS
80 → HTTP
443 → HTTPS

B) Registered Ports (1024–49151)
Used by different applications.
Examples:
3306 → MySQL
5432 → PostgreSQL
8080 → Alternative HTTP

C) Dynamic / Ephemeral Ports (49152–65535)
Temporary ports.
Automatically assigned by the operating system.
Mainly used by clients while communicating with servers.
Released after the connection ends.
Example:
Your Laptop
Temporary Port → 52341 
         ↓
Google Server
Port → 443

5. What is Port 0?
Port 0 is reserved.
Not used for normal network services.
Ignore Port 0 while scanning

6. Open Port
An Open Port means a service/application is actively listening for incoming connections.
Example:
Port 443 Open → HTTPS service is running.

7. Closed Port
A Closed Port means no service is listening on that port.
Any connection request will fail.

8. Common Ports
SSH (Port 22)
SSH = Secure Shell
Used for secure remote login to another computer.

DNS (Port 53)
DNS = Domain Name System
Converts:
Website Name → IP Address

HTTP (Port 80)
HTTP = HyperText Transfer Protocol
Used to transfer webpages.
Data is not encrypted.

HTTPS (Port 443)
HTTPS = HyperText Transfer Protocol Secure
Secure version of HTTP.
Data is encrypted.

9. Client vs Server
Server
Provides services.
Keeps ports open.
Waits for incoming requests.
Example:
Google Server
Port 443 → Open
Client
Requests services.
Does not normally keep ports like 80 or 443 open.
Operating system automatically assigns a temporary (ephemeral) port.
Example:
Your Laptop
Port 53124
    ↓
Google Server
Port 443

10. One Port = One Service
One port normally runs one service only.
Example:
Port 443 → HTTPS
Port 443 cannot normally run SSH and HTTPS simultaneously on the same IP.

11. One Service Can Handle Millions of Clients
A single service can communicate with millions of clients simultaneously.
Example:
Google uses Port 443 for millions of users.

Each connection is unique because of:
Client IP
Client Port
Server IP
Server Port
"""
"""
Yes, bro. For your Network Scanner V1, this TCP & UDP knowledge is completely enough. ✅

Later, if you build an advanced scanner (SYN Scan, FIN Scan, UDP Scan, etc.), you'll learn more. But for Version 1, this is all you need.


---
TCP & UDP 
1. What is a Protocol?
A Protocol is a set of rules that tells devices how to communicate with each other.
Without protocols, computers cannot understand each other.

2. What is TCP?
TCP = Transmission Control Protocol
It is a reliable communication protocol.
It ensures data reaches the destination correctly

3. Features of TCP
Reliable data transfer.
Connection-Oriented.
Checks for errors.
Retransmits lost data.
Delivers data in the correct order.
Slower than UDP because of additional checking.

4. What is Connection-Oriented?
TCP first establishes a connection between the sender and receiver.
After the connection is established, data transfer begins.
Example:
Client
   ↓
Connection Established
   ↓
Data Transfer

5. What is UDP?
UDP = User Datagram Protocol
It is a fast communication protocol.
It sends data without establishing a connection.

6. Features of UDP
Very fast.
Connectionless.
No guarantee that data will reach the destination.
No retransmission of lost data.
Data may arrive out of order.
Uses fewer system resources.

7. What is Connectionless?
UDP sends data immediately.
No connection setup before sending data.
Example
Client
   ↓
Data Sent Immediately

8. Where is TCP Used
HTTP
HTTPS
SSH
Email
FTP
Banking Websites
File Transfer

Reason:
Data accuracy is important.

9. Where is UDP Used?
Online Games
Voice Calls
Video Calls
Live Streaming
Live Broadcasting

Reason:
Speed is more important than perfect delivery.

10. Important Difference
TCP is Reliable but NOT Secure.
HTTPS is Secure because it uses TLS/SSL encryption over TCP.
Reliability and security are different concepts.

11. Why Does a Network Scanner Use TCP?
TCP establishes a connection with the target port.
If the connection succeeds:
Port is Open.
If the connection fails:
Port is Closed.
Therefore, TCP scanning is simple and reliable.

12. Why Not UDP?
UDP does not establish a connection.
No clear success or failure response.
Determining whether a UDP port is open is much more difficult.
UDP scanning is more advanced and not required for Network Scanner V1.

"""
