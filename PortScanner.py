#!/usr/bin/python

from socket import *
import optparse
from threading import *
from termcolor import colored

def connScan(tgtHost, tgtPort):

	try:
		sock = socket(AF_INET,SOCK_STREAM)
		sock.connect((tgtHost,tgtPort))
		print (colored('[*] %d/tcp is open' % (tgtPort), 'red'))
	except:
		print (colored('[-] %d/tcp is closed' % (tgtPort),'green')) 
	finally:
		sock.close()


def portscan(tgtHost, tgtPorts):
	try :
		tgtIP = gethostbyname(tgtHost)
	except:
		print ('Unknown Host %s' %(tgtHost))
	try:
		tgtname = gethostbyaddr(tgtIP)
		print ('[*] Scan results for :' + tgtIP)
	except:
		print ('[*] Scan results for :' + tgtname[0])
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target = connScan, args=(tgtHost,int(tgtPort)))
		t.start()

def main():
	parser = optparse.OptionParser('Program usage: ' + '-H <Target Host> -p <Target Ports>')
	parser.add_option('-H', dest = 'tgtHost' , type = 'string', help = 'Specify Target host')
	parser.add_option('-p', dest = 'tgtPort' , type = 'string', help = 'Specify Target ports seperated by comma')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None):
		print (parser.usage)
		exit(0)
	portscan(tgtHost, tgtPorts)
if __name__== '__main__':
	main()
