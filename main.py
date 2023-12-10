#Copyright © 2023 just1nn1t
#All rights reserved. This project is licensed under GitHub's default copyright laws,
#meaning that I retain all rights to my source code and no one may reproduce, distribute, or create derivative works from my work.
#This tool is meant for research and educational purposes only and any malicious usage of this tool is prohibited.

from scapy.all import *
import paramiko

#you may change it
address = 'serverip'
usrname = 'username'
passwd = 'password'
path = '/path/to/cred.txt'

def handlepacket(packet):
	if packet.haslayer(Dot11):
		data = {}
		#get SSID
		ssid = packet[Dot11Elt].info.decode('utf-8', 'ignore')
			if ssid:
				data['SSID'] = ssid
		#get BSSID
		bssid = packet[Dot11].addr2
		if bssid:
			data['BSSID'] = bssid
		#get security mode
		if packet.haslayer(Dot11WEP):
			data['Security Mode'] = "WEP"
		elif packet.haslayer(Dot11Beacon) and packet.getlayer(Dot11Beacon).cap.privacy:
			data['Security Mode'] = "WPA or WPA2"
		elif packet.haslayer(Dot11WPA3_Enterprise) or packet.haslayer(Dot11WPA3_Personal):
			data['Security Mode'] = "WPA3"
		else:
			data['Security Mode'] = "Open"
		#get channel no.
		channel = packet.getlayer(RadioTap).Channel
		if channel:
			data['Channel'] = channel
		sendto(data)

def sendto(data):
	try:
		#connect to server
		transport = paramiko.Transport((address, 22))
		transport.connect(username=usrname, password=passwd)
		sftp = paramiko.SFTPClient.from_transport(transport)
        
		#write to file
		with sftp.file(path, 'a') as f:
			for key, value in data.items():
				f.write(f"{key}: {value}\n")

		sftp.close()
		transport.close()
		print("Data sent to the server.")
	except Exception as e:
		print(f"Error: {e}")

sniff(iface='wlan0', prn=handlepacket)