# Oculus

Oculus is a tool for wardriving. It utilizes the 'Scapy' library for wardriving, capturing and analyzing Wi-Fi packets. It extracts information (such as SSID, BSSID, security mode, and channel) from the packet and then securely sends this data to a specified server in real-time using SSH ('paramiko' library), appending the information to the 'cred.txt' file.

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

## Setup a SFTP server

```bash

(in this case in Ubuntu/Debian)

Install OpenSSH server:
sudo apt-get update
sudo apt-get install openssh-server

Edit configuration file (usually located at /etc/ssh/sshd_config):
sudo nano /etc/ssh/sshd_config
subsystem sftp internal-sftp <-- make sure it's there or uncommented

Restart SSH service:
sudo service ssh restart

Create SFTP user:
sudo adduser <your_username>

Test it by:
sftp <your_username>@<your_server_ip>

```

## Warning& license
Copyright © 2023 just1nn1t

All rights reserved. This project is licensed under GitHub's default copyright laws, meaning that I retain all rights to my source code and no one may reproduce, distribute, or create derivative works from my work.

Only use this software according to your current legislation. Misuse of this software can raise legal and ethical issues which I don't support nor can be held responsible for.
