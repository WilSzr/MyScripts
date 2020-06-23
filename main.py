#!usr/bin/env python

import csv
import sys
import itertools
import os
import time
from telnet_func import telnet_vz
from ssh_func import ssh_vz
import getpass


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

#user = 'amersp-wilszr'
#pw = 'AmerspJul2020.'
    

def get_cred():     
	user = getpass.getuser()     
	password = getpass.getpass()     
	return {'user' : user, 'password' : password} 

def main():
	
	cred = get_cred() 	
	user = cred["user"] 	
	pw = cred["password"]

	for ip in flat_list:
	
		try:    
			print ip + ' TELNET'
			telnet_vz(ip,user,pw,cmd_list,output_text)
		
		except:
			try:
				print ip + ' SSH'
				ssh_vz(ip,user,pw,cmd_list,output_text)      
			
			except:
				print ('\n***** No connection to ' + ip + ' ***** \n')
				f = open(output_text,'a')
				f.write('\n***** No connection to ' + ip + ' ***** \n')
				f.write('\n' + '=' * 120 + '\n')
				f.close()

if __name__ == '__main__':
	main()


