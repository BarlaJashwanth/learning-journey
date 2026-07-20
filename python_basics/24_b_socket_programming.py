"""
sockets :
1. What is a Socket?
A socket is a software communication endpoint.
It allows two computers/programs to communicate over a network.
Without a socket, network communication is not possible.
Simple Definition:
> A socket is a communication endpoint used for network communication.

2. Why do we need Sockets?
Sockets are used to:
Connect to another computer.
Send data.
Receive data.
Close the connection after communication.

3. Is Socket a Python Concept?
No.
Socket is provided by the Operating System (OS).
Python only provides the socket module to use OS sockets.
Other languages like Java, C, C++, C#, Go, and Rust also use OS sockets.

4. Types of Sockets (For Our Project)
Client Socket
Initiates the connection.
Example: Network Scanner.

Server Socket
Waits for incoming connections.
Example: Google Web Server.

5. Both Client and Server Use Sockets
Client Socket  ⇄  Server Socket
Both sides create sockets to communicate.

6. Socket Communicates Using
IP Address + Port Number
Example:
142.250.xxx.xxx : 443
IP → Identifies the computer.
Port → Identifies the service.

7. Port vs Socket
Port
A numbered door.
Example: 22, 80, 443.
Exists on the server.
Does not communicate by itself.

Socket
A communication endpoint created by software.
Uses the port to communicate.

8. Server Socket vs Port
They are not the same.
Example:
Port 443
↓
HTTPS Program
Server Socket (Listening)
Port = Door Number.
Server Socket = Listener standing at that door.

9. Socket Protocols
A socket can use:
TCP ✅
UDP ✅
For Network Scanner V1, we'll use TCP sockets.

10. Does Socket Need Internet?
No.
A socket can be created even without internet.
Communication can happen over:
Internet
Local Area Network (LAN)
If there is no network path, the connection attempt fails.

11. Socket Flow in Network Scanner
Create Client Socket
↓
Connect to IP + Port
↓
Connected?
↓
Yes → Port Open
No → Port Closed
↓
Close Socket

12. Real-Life Analogy
Building = IP Address
Door Number = Port
Person Standing at Door = Server Socket
Visitor = Client Socket
"""
import socket
# importing of socket as it is inbuilt module

s = socket.socket() # CREATING OF SOCKET
# first socket explains us which module to be used and second socket is function inside the socket module
print(s)
# output : <socket.socket fd=336, family=2, type=1, proto=0>
# socket.socket : means socket successfully created
# family 2 : means "socket.AF_INET" AF_INET means IPv4
# type 1 : means "socket.SOCK_STREAM" which means by default it is TCP Socket

## AF : means "Address family" , INET : Internet (IPv4)
## SOCK_STREAM = TCP (continuous stream)
## SOCK_DGRAM = UDP (datagram)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

s.connect(("google.com",80))
print("connected successfully")

"""
This above code runs successfully and you get printed successfully as the python succesffully took a socket from windows od
and then tried to connect google port 80 and it succeeded and printed next code of connected succesfully

"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.settimeout(1)
    s.connect(("google.com",45))
    print("connected successfully")
except TimeoutError :
    print("no connection")

"just s.connect(()) , we need to open a socket first and then establish a connection ."

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    x = int(input(f"enter your port number to be scanned:"))
    s.settimeout(2)
    s.connect(("google.com",x))
    print("connected successfully")
except TimeoutError :
    print("no connection")
s.close()
print("socket closed")

# s.settimeout() Helps us for seconds it should wait for response ...

s.close() # this makes socket get closed after work
"""
what happens if we wont close sockets then it may lead to big confusion
. resources stay occupied 
. the operating system keeps the connection open for some time
. too many open sockets can slow programs or eventually cause errors
"""

### Exception handling in socket programing
# mainly for timeout error , oserror

