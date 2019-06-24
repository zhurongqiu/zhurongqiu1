import re

mac_table = '166   54a2.74f7.0326   DYNAMIC   Gi1/0/11'

mac_info = re.match('(\d{1,4})\s+(\w{1,4}\.\w{1,4}\.\w{1,4})\s+\s(\w*)\s+(\w*/\d*/\d*)',mac_table).groups()



print(mac_table)
print('-'*60)
print('%-12s : %s'%('VLAN ID',mac_info[0]))
print('%-12s : %s'%('MAC',mac_info[1]))
print('%-12s : %s'%('Type',mac_info[2]))
print('%-12s : %s'%('Interface',mac_info[3]))