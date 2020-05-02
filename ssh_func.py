#!usr/bin/env python

# SSH function that expects to get passed the ip address of the device to connect

def ssh_vz(ip):

    """
    This fuction needs the IP addresses to be passed as well as the username and 
    password of the user. 
    """

    twrssh = paramiko.SSHClient()
    twrssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    twrssh.connect(ip, port=22, username=user, password=pw)
    print '\n***** SSH connection successfull to ' + ip + ' ****** \n'

    remote = twrssh.invoke_shell()

    for c in cmd_list:
        remote.send(c + '\n')
        time.sleep(1)
   
    remote.send('exit\n')
    time.sleep(1)    
   
    buf = remote.recv(65000)

    print buf
    print ('\n' + '=' * 120 + '\n')

    f = open(output_text,'a')
    f.write('\n***** SSH connection to ' + ip + ' ***** \n\n' )
    f.write(buf) 
    f.write('\n' + '=' * 120 + '\n')
    f.close()
    
    twrssh.close()