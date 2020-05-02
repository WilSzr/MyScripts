#!usr/bin/env python

# Telnet function that expects to get passed the ip address of the device to connect

def telnet_vz(ip):

	"""
    This fuction needs the IP addresses to be passed as well as the username and 
    password of the user. 
    """

    t = telnetlib.Telnet(ip)
    t.read_until(b"Username:")
    t.write(user.encode("ascii") + b"\n")

    if pw:
        t.read_until(b"Password:")
        t.write(pw.encode("ascii") + b"\n")
        print '\n***** TELNET connection successfull to ' + ip + ' ***** \n'

    for c in cmd_list:
        t.write(c + "\n")

    t.write(b"exit\n")

    text = t.read_all()

    print text
    print ('\n' + '=' * 120 + '\n')

    f = open(output_text,'a')
    f.write('\n***** TELNET connection to ' + ip + ' ***** \n')
    f.write(text) 
    f.write('\n' + '=' * 120 + '\n')
    f.close()