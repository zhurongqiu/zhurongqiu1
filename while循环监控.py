import re
import os
import time

while True:
  show_netstat = os.popen('netstat -anvp tcp').read()
  netstat_info1 = re.findall('(\*\.80\s)',show_netstat)
  if netstat_info1:
    print('http(tcp/80)服务已经被打开')
    break
  else:time.sleep(1),print('等待一秒重新开始监控')




