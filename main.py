#!usr/bin/env python

import csv
import sys
import itertools
import paramiko
import os
import time
from telnet_func import telnet_vz
from ssh_func import ssh_vz


with open ('just_ip_cat2.csv','rb') as t:
    reader = csv.reader(t)
    ips = list(reader)

flat_list = list(itertools.chain(*ips))

with open('commands_list.csv','rb') as cm:
    reader = csv.reader(cm)
    cms = list(reader)

cmd_list = list(itertools.chain(*cms))

output_text = 'complete_vrf_bfd.txt'

print flat_list 
print '\n'
print cmd_list
print '\n'

user = 'amersp-wilszr'
pw = 'AmerspMay2020.'

#def telnet_vz(ip):
#
#    t = telnetlib.Telnet(ip)
#    t.read_until(b"Username:")
#    t.write(user.encode("ascii") + b"\n")
#
#    if pw:
#        t.read_until(b"Password:")
#        t.write(pw.encode("ascii") + b"\n")
#        print '\n***** TELNET connection successfull to ' + ip + ' ***** \n'
#
#    for c in cmd_list:
#        t.write(c + "\n")
#
#    t.write(b"exit\n")
#
#    text = t.read_all()
#
#    print text
#    print ('\n' + '=' * 120 + '\n')
#
#    f = open(output_text,'a')
#    f.write('\n***** TELNET connection to ' + ip + ' ***** \n')
#    f.write(text) 
#    f.write('\n' + '=' * 120 + '\n')
#    f.close()
#
#def ssh_vz(ip):
#
#    twrssh = paramiko.SSHClient()
#    twrssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#    twrssh.connect(ip, port=22, username=user, password=pw)
#    print '\n***** SSH connection successfull to ' + ip + ' ****** \n'
#
#    remote = twrssh.invoke_shell()
#
#    for c in cmd_list:
#        remote.send(c + '\n')
#        time.sleep(1)
#   
#    remote.send('exit\n')
#    time.sleep(1)    
#   
#    buf = remote.recv(65000)
#
#    print buf
#    print ('\n' + '=' * 120 + '\n')
#
#    f = open(output_text,'a')
#    f.write('\n***** SSH connection to ' + ip + ' ***** \n\n' )
#    f.write(buf) 
#    f.write('\n' + '=' * 120 + '\n')
#    f.close()
#    
#    twrssh.close()
    

def main():

	for ip in flat_list:
	
		try:    
			print ip + ' TELNET'
			telnet_vz(ip)
		
		except:
			try:
				print ip + ' SSH'
				ssh_vz(ip)      
			
			except:
				print ('\n***** No connection to ' + ip + ' ***** \n')
				f = open(output_text,'a')
				f.write('\n***** No connection to ' + ip + ' ***** \n')
				f.write('\n' + '=' * 120 + '\n')
				f.close()

if __name__ == '__main__':
    main()


