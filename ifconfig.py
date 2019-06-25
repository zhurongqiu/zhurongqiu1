import os
import re
import IPy

ifconfig_result = os.popen('ifconfig ' + ' en0').read()

# 正则表达式查找ip，掩码，广播和mac地址
ipv4_add = re.findall('\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) ', ifconfig_result)[0]
netmask = re.findall('[0][x]\w[0-9a-fA-F]{1,8}', ifconfig_result)[0]
broadcast = re.findall('\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\n', ifconfig_result)[0]
mac_addr = re.findall('\w*[0-9a-f]\:\w*[0-9a-f]\:\w*[0-9a-f]\:\w*[0-9a-f]\:\w*[0-9a-f]\:\w*[0-9a-f]\s', ifconfig_result)[0]

# 格式化字符串
format_string = '{0:<20}:{1:<20}'

# 打印结果
print(format_string.format('ipv4_add', ipv4_add))
print(format_string.format('netmask', str(IPy.IP(int(netmask, 16)))))
print(format_string.format('broadcast', broadcast))
print(format_string.format('mac_addr', mac_addr))

# 产生网关的ip地址
ipv4_gw = (re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.)', ipv4_add)[0] + '1')

# 打印网关的ip地址
print('\n我们假设网关ip地址最后一位为1，因此网关ip地址为：' + ipv4_gw + '\n')

# ping网关
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()

re_ping_result = re.search('(.*)=(.*)\w', ping_result)[0]

print(re_ping_result)
if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达')
