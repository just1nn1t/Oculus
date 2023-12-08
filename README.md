# Oculus

Oculus utilizes the 'Scapy' library for wardriving, capturing and analyzing Wi-Fi packets. It extracts information (such as SSID, BSSID, security mode, and channel) from the packet and then securely sends this data to a specified server in real-time using SSH (paramiko library), appending the information to a 'cred.txt' file.
