import re

str1 = 'Port-channel1.189         192.168.189.254  YES       CONFIG   UP                   up'


network_info = re.match('\s*(\w.*\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w*)\s+(\w*)\s+(\w*)\s+(\w*)\s*',str1).groups()


print(network_info)
print('_'*80)
print('%-7s : %s'%( '接口',network_info[0]))
print('%-7s : %s'%( 'IP地址',network_info[1]))
print('%-7s : %s'%( '状态' ,network_info[-1]))