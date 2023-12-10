# Oculus

Oculus is a tool for wardriving with Raspberry pi. It utilizes the 'Scapy' library for wardriving, capturing and analyzing Wi-Fi packets. It extracts information (such as SSID, BSSID, security mode, and channel) from the packet and then securely sends this data to a specified server in real-time using SSH ('paramiko' library), appending the information to the 'cred.txt' file.

## Installation

```bash
git clone https://github.com/just1nn1t/Oculus.git
```

## Requirements

```python

pip install scapy
pip install paramiko

sudo ifconfig <interface> down
sudo iwconfig <interface> mode monitor
sudo ifconfig <interface> up

```

## Warning& license
Copyright © 2023 just1nn1t

All rights reserved. This project is licensed under GitHub's default copyright laws, meaning that I retain all rights to my source code and no one may reproduce, distribute, or create derivative works from my work.

Only use this software according to your current legislation. Misuse of this software can raise legal and ethical issues which I don't support nor can be held responsible for.
