import paramiko
import re

def qytang_ssh(ip,username,password,port=22,cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port=port,username=username,password=password,timeout=5,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

def ssh_get_route(ip,username,password,port=22,cmd='route -n'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port=port,username=username,password=password,timeout=5,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    route_info = stdout.read().decode()
    route_Gateway = re.findall('0.0.0.0\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*UG',route_info)[0]
    return route_Gateway


if __name__ == '__main__':
    print(qytang_ssh('192.168.1.77','root','36593659Forget'))
    print(qytang_ssh('192.168.1.77', 'root','36593659Forget',cmd='pwd'))
    print('网关为')
    print(ssh_get_route('192.168.1.77', 'root','36593659Forget',))


