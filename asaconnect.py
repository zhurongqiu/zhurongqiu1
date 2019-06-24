import re

show_conn = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710,idle 0:01:09,bytes 27575949,flags UIO'


conn_info = re.match('(\w*)\s+'                                    #0 连接类型（tcp活着udp）
                     '(\w*)\s+'                                    #1 server
                     '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d*)\s+' #2 目的ip地址以及端口
                     '(\w*)\s+'                                    #3 localserver
                     '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d*)+'   #4 本地源ip地址以及端口
                     '\S(\w*)'                                     #5 idle
                     '\s(\d)+'                                     #6 小时
                     '\:'                                          #7 :
                     '(\d\d)+'                                     #8 分钟
                     '\:'                                          #9 ：
                     '(\d\d)+'                                     #10 秒
                     '\S(\w*)+'                                    #11 bytes    
                     '\s(\d{1,})+'                                 #12 字节数
                     '\S(\w*)'                                     #13 flag
                     '\s(\w*)'                                     #14 标记
                     '',show_conn).groups()


print(show_conn)
print('*'*60)
print('%-20s : %s '%('protocol',conn_info[0]))
print('%-20s : %s '%('server',conn_info[2]))
print('%-20s : %s '%('localserver',conn_info[4]))
print('%-20s : %s小时 %s分钟 %s秒 '%('idle',conn_info[6],conn_info[7],conn_info[8]))
print('%-20s : %s '%('bytes',conn_info[-3]))
print('%-20s : %s '%('flags',conn_info[-1]))