import subprocess
# used for interfacing python with cmd terminal

dnsFlush = "ipconfig /flushdns"
subprocess.run(dnsFlush, capture_output=True, text=True).stdout
# clear the dns cache

reconnect = "netsh wlan connect ssid=eduroam name=eduroam"
subprocess.run(reconnect, capture_output=True, text=True).stdout
# restart the wifi connection

