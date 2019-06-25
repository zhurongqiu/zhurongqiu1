import IPy
import os

num_16 = 0xffffff00

num_16str = '0xffffff00'

#num_16int = int(num_16str,16)
result = IPy.IP(int(num_16str,16))

print(str(result))

ipv4_gw = '192.168.31.1'
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()

print(str(ping_result))