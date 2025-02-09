
import socket

def scan(target, ports):
	print('\n' + ' Starting Scan ' + str(target))
	for port in range(1,ports):
		scanning (target,port)
		print('Scanning....')
        


def scanning (ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print(" Port Opened " + str(port))
		sock.close()
	except:
		pass


targets = input("  Enter Targets To Scan: ")
ports = int(input("  Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print("  Scanning Ports")
	for ip  in targets.split(','):
		scan(ip.strip(' '), ports)
else:
	scan(targets,ports)