import re
import os

route_n_result = os.popen('netstat -rn').read()


route_gw = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s*UGSc',route_n_result)[0]


print('%s:%s'%('网关为',route_gw[0:16]))