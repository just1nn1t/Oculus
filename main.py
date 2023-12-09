#Copyright © 2023 just1nn1t
#All rights reserved. This project is licensed under GitHub's default copyright laws,
#meaning that I retain all rights to my source code and no one may reproduce, distribute, or create derivative works from my work.
#This tool is meant for research and educational purposes only and any malicious usage of this tool is prohibited.

from scapy.all import RadioTap, Dot11Elt, Dot11, sniff
import paramiko

#you may change it
address = 'serverip'
username = 'username'
password = 'password'
path = '/path/to/cred.txt'

def getcred(packet):
	credentials = {}

	ssid = getssid(packet)
	if ssid:
		credentials['SSID'] = ssid

	bssid = getbssid(packet)
	if bssid:
		credentials['BSSID'] = bssid

	secmode = getsecmode(packet)
	if secmode:
		credentials['Security Mode'] = secmode

	channel = getchannel(packet)
	if channel:
		credentials['Channel'] = channel

	return credentials


def getssid(packet):
	if not isinstance(packet, RadioTap) or not isinstance(packet.payload, Dot11Elt):
		return None
	#SSID from packet
	ssid = packet.payload.info.decode('utf-8', 'ignore')
	return ssid


def getbssid(packet):
	if not isinstance(packet, RadioTap) or not isinstance(packet.payload, Dot11):
		return None
	#BSSID from packet
	bssid = packet.payload.addr2
	return bssid


def getsecmode(packet):
	if not isinstance(packet, RadioTap) or not isinstance(packet.payload, Dot11):
		return None
	#security mode from packet
	if packet.haslayer(Dot11WEP):
		secmode = "WEP"
	elif packet.haslayer(Dot11Beacon) and packet.getlayer(Dot11Beacon).cap.privacy:
		secmode = "WPA or WPA2"
	elif packet.haslayer(Dot11WPA3_Enterprise) or packet.haslayer(Dot11WPA3_Personal):
		secmode = "WPA3"
	else:
		secmode = "Open"
	return secmode


def getchannel(packet):
	if not isinstance(packet, RadioTap):
		return None
	#channel no. from packet
	channel = packet.Channel
		return channel


def sendto(credentials)):
	try:
		transp = paramiko.Transport((address, 22))
		transport.connect(username=username, password=password)
		sftp = paramiko.SFTPClient.from_transport(transport)
        
		with sftp.file(path, 'a') as f:
			for key, value in credentials.items():
				f.write(f"{key}: {value}\n")

		sftp.close()
		transport.close()
		print("Data sent to the server.")
	except Exception as e:
		print(f"Error: {e}")


def handlepacket(packet):
	credentials = getcred(packet)
	if credentials:
		sendto(credentials)

#replace 'wlan0' with your wifi interface
sniff(iface='wlan0', prn=handlepacket)
