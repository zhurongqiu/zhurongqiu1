import re

mac_table = '166   54a2.74f7.0326   DYNAMIC   Gi1/0/11'

mac_info = re.match('(\d{1,4})\s+'                      #匹配vlan id
                    '(\w{1,4}\.\w{1,4}\.\w{1,4})\s+'    #匹配mac地址
                    '\s(\w*)\s+'                        #匹配type
                    '(\w*/\d*/\d*)'                     #匹配接口
                    '',mac_table).groups()



print(mac_table)
print('-'*60)
print('%-12s : %s'%('VLAN ID',mac_info[0]))             #打印vlan id
print('%-12s : %s'%('MAC',mac_info[1]))                 #打印mac地址
print('%-12s : %s'%('Type',mac_info[2]))                #打印type
print('%-12s : %s'%('Interface',mac_info[3]))           #打印接口信息