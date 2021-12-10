import subprocess

dnsFlush = "ipconfig /flushdns"
subprocess.run(dnsFlush, capture_output=True, text=True).stdout

reconnect = "netsh wlan connect ssid=eduroam name=eduroam"
subprocess.run(reconnect, capture_output=True, text=True).stdout

