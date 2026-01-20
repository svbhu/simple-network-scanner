import socket
import sys
from datetime import datetime

# 1. Define the target
# We ask the user for an IP address or hostname (like 'google.com' or '192.168.1.1')
target = input("Enter the target IP address to scan: ")

# 2. Resolve the hostname to an IP address
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

print("-" * 50)
print(f"Scanning Target: {target_ip}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

try:
    # 3. Scan ports 1 to 1024 (Common ports)
    # You can increase the range to 65535 to scan all ports
    for port in range(1, 1025):
        # Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout so the script doesn't hang on filtered ports (0.5 seconds)
        s.settimeout(0.5)
        
        # connect_ex returns 0 if the connection is successful (Port is OPEN)
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
            
        # Close the socket to free up resources
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()

except socket.error:
    print("\nCould not connect to server.")
    sys.exit()

print("-" * 50)
print("Scanning completed.")