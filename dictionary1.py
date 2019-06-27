import re

asa_conn = 'TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n' \
           'TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO'

asa_info = asa_conn.split('\n')
dic_listall = {}
print(asa_info[0])
print(asa_info[1])

print('打印字典')

for i in asa_info:
      asaconn = re.match('(\w*)\s+'                                    
                     '(\w*)\s+'                                    
                     '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                     ':(\d*)'                                        
                     '\s(\w*)\s+'                                    
                     '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                     ':(\d*)'   
                     '\S\s(\w*)'                                     
                     '(\s\d*:\d*:\d*)'                                     
                     ',\s(\w*)\s+'                                    
                     '(\d*)'                                 
                     ',\s(\w*)\s+'                                    
                     '(\w*)'                                     
                     '',i).groups()
      dic_list = {(asaconn[2],asaconn[3],asaconn[5],asaconn[6]):(asaconn[10],asaconn[12])}
      dic_listall = dic_listall.copy()
      dic_listall.update(dic_list)
print(dic_listall)

print('格式化打印输出')
for key,value in dic_listall.items():
      print('%12s:%-20s|%12s:%-12s|%12s:%-20s|%12s:%-12s|\n%12s:%-20s|%12s:%-12s'%('src',key[0],'src_p',key[1],'dest',key[2],'dest_p',key[3],'bytes',value[0],'flags',value[1]))
      print('-'*120)