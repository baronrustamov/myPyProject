"""
MyScript
This script is very useful for when you just to do a health check on a remote server. It does the followings:
  - NSLOOKUP
  - PING to see if the site is up
  - Certificate/SSL/TLS info
"""

import socket
import hashlib
import os
import time
import calendar  # module of python to provide useful fucntions related to calendar
import datetime  # module of python to get the date and time
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen, ssl, socket
from time import strftime

class Laptop:
	name = 'My Laptop'
	processor = 'Intel Core'
	@staticmethod
	def start():
		PrintToConsole('Laptop is starting..', 'red')
		#print('Laptop is starting..')
		#return 'Laptop is starting..'
	def restart(self):
		PrintToConsole('Laptop is restarting..', 'red')
		#print('Laptop is restarting')
	def details(self):
		#print('My laptop name is:', self.name)
		#print('It has',self.processor,'processor.')
		self.outname = ('My laptop name is: ' + self.name)
		self.outproc = ('It has ' + self.processor + ' processor.')
		PrintToConsole(self.outname, 'red')
		PrintToConsole(self.outproc, 'red')

class Getip:
	def __init__(self):
		wan_ip = self.get_wan_ip()
		lan_ip = self.get_local_ip()
	def get_wan_ip(self):
			w_ip = urlopen('http://ipecho.net/plain').read().decode('utf-8')
			#print("External IP: ", w_ip)
			self.wan_ip = w_ip
			#return w_ip
	def get_local_ip(self):
		try:
			l_ip = (socket.gethostbyname(socket.gethostname()))
			#print("Internal IP: ", l_ip)
			self.lan_ip = l_ip
		except:
			#res.configure(text='Unkown Error', fg='#red')
			self.lan_ip = 'none'

class ServerHealthCheck():
	SHCLog = ""
	def __init__(self, base_url, port, tcp):
		self.base_url = base_url
		self.ip_now = self.obtain_ip()
		self.port = port
		self.tcp = tcp
		self.url_path = self.tcp + "://" + base_url
		self.ping_host()
		#self.obtain_http_info()
		#self.obtain_cert_info()

	def obtain_ip(self):
		print("\n"+"__LOOKUP____________________________________________")
		self.SHCLog = "_____________________LOOKUP_______________________________"+"\n"
		currnet_ip = socket.gethostbyname(self.base_url)
		print("ip: " + currnet_ip)
		self.SHCLog = self.SHCLog + "ip: " + currnet_ip + "\n"
		print("FQDN: " + socket.getfqdn(self.base_url))
		self.SHCLog = self.SHCLog + "FQDN: " + socket.getfqdn(self.base_url) + "\n"
		distinct_ips = []
		# 0,0,0,0  is for (family, type, proto, canonname, sockaddr)
		socket_info = socket.getaddrinfo(self.base_url, 0, 0, 0, 0)
		for result in socket_info:
			ns_ip = result[4][0]
			if distinct_ips.count(ns_ip) == 0:
				distinct_ips.append(ns_ip)
				print(ns_ip)
		distinct_ips = list(set(distinct_ips))
		return currnet_ip

	def ping_host(self):
	# ping reesult
		print("\n" + "__PING INFO____________________________________________")
		self.SHCLog = self.SHCLog + ("\n" + "_____________________PING INFO____________________________________________" + "\n")
		self.SHCLog = self.SHCLog + "Pinging: " + self.ip_now + "\n"
		response = os.system("ping -n 2 " + self.ip_now)
		self.SHCLog = self.SHCLog + "/n"
	#OLD# response = os.system("ping -c 1 " + self.ip_now)
		# and then check the response...
		if response == 0:
			print("\n" + "Server " + self.base_url + ": is up ")
			self.SHCLog = self.SHCLog + "server " + self.base_url + ": is UP " + "\n"
		else:
			print("\n" + "Server " + self.base_url + ": is DOWN !!!")
			self.SHCLog = self.SHCLog + "server " + self.base_url + ": is DOWN !!!" + "\n"
'''
	def obtain_http_info(self):
		print("\n"+"__SSL/TLS INFO____________________________________________")
		req = Request(self.url_path)
		try:
			response = urlopen(req, context=ssl._create_unverified_context())
			# htmlSource = response.read()
		except HTTPError as e:
			print('The server couldn\'t fulfill the request.')
			print('Error code: ', e.code)
		except URLError as e:
			print('We failed to reach a server.')
			print('Reason: ', e.reason)
		else:
			print("http code:" + str(response.getcode()))

	def obtain_cert_info(self):
		context = ssl.create_default_context()
		with socket.create_connection((self.base_url, self.port)) as socket_connection:
			with context.wrap_socket(socket_connection, server_hostname=self.base_url) as server_socket:
				# uncomment to print everything
				# print(json.dumps(server_socket.getpeercert() , indent=2, sort_keys=True))
				cert_info = server_socket.getpeercert()
				subject = dict(x[0] for x in cert_info['subject'])
				issued_to = subject['commonName']
				issuer = dict(x[0] for x in cert_info['issuer'])
				issued_by = issuer['commonName']
				valid_from = cert_info['notBefore']
				valid_to = cert_info['notAfter']
				serial_number = cert_info['serialNumber']
				der_cert = server_socket.getpeercert(False)
				der_cert_bin = server_socket.getpeercert(True)
				pem_cert = ssl.DER_cert_to_PEM_cert(server_socket.getpeercert(True))
				# uncomment the below line if you want to see the actual public cert
				# print("certificate pub:",pem_cert)
				thumb_md5 = hashlib.md5(der_cert_bin).hexdigest()
				thumb_sha1 = hashlib.sha1(der_cert_bin).hexdigest()
				thumb_sha256 = hashlib.sha256(der_cert_bin).hexdigest()
				print("issued_to: " + issued_to)
				print("issued_by: " + issued_by)
				print("valid_from: " + valid_from)
				print("valid_to: " + valid_from)
				print("MD5: " + thumb_md5)
				print("SHA1: " + thumb_sha1)
				print("SHA256: " + thumb_sha256)
				print("cipher: " + str(server_socket.cipher()))
				print("SSL/TLS version:  " + server_socket.version())
				print("serial_number: " + serial_number)
				# print(server_socket.shared_ciphers())
			server_socket.close()
'''

class Int:
	n1 = 0
	n2 = 0
	CResult = ""
	def read(self):
		# read integer from user
		self.n1 = int(input('Enter a number: '))
		self.n2 = int(input('Enter another number: '))
	def write(self):
		print('The sum of two numbers is:', self.n1 + self.n2)
		if self.n1 < self.n2:
			self.CResult = self.n1, 'is less than', self.n2
			return self.CResult
		else:
			self.CResult = (self.n1, 'is not less than', self.n2)
			return self.CResult

class HelloName:
	def hello():
		# read multiple strings from user
		firstName = input('Enter your first name: ')
		lastName = input('Enter your last name: ')
		#print('Hello', firstName, lastName, "\n")
		return "Hello, " + firstName + " " + lastName

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class WriteToFile:
	def write():

		print("Writing info to sample.txt")
		print("File sample.txt is opened.")

		# OpenFileToWriteOutput
		with open('2output.txt', 'a') as out:
		#out.write(var + '\n')
			# Hello
			out.write(hello1 + '\n' + '\n')
			# DateTime
			out.write("Current Time is: " + timestring + '\n' + '\n')
			# Laptop
			out.write("Your Laptop is: " + laptop1.name + ' ' + laptop1.processor + '\n' + '\n')
			# NumbersCompare (Int Class)
			out.write('Your numbers are: ' + str(Int1.n1) + ' and ' + str(Int1.n2) + '\n')
			out.write("Comparison: " + str(Int1.CResult) + '\n' + '\n')
			# UrlopenHost
			out.write('Your host is: ' + host_name + '\n')
			# SiteHealthCheckResultsv
			out.write(serverHealthCheck.SHCLog + '\n')
			# StopWatchStats
			out.write('Total Time: ' + str(round(endtime - starttime, 2)) + ' secs' + '\n')
			# CloseFile
			out.close()

		print("File sample.txt is closed.")
		print("File sample.txt successfully updated!")

def findDay(date):
	born = datetime.datetime.strptime(date, '%d %m %Y').weekday() #this statement returns an integer corresponding to the day of the week
	return (calendar.day_name[born]) #this statement returns the corresponding day name to the integer generated in the previous statement

def print_format_table(): #prints table of formatted text format options
	for style in range(8):
		for fg in range(30,38):
			s1 = ''
			for bg in range(40,48):
				format = ';'.join([str(style), str(fg), str(bg)])
				s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
			print(s1)
		print('\n')

def pause():
	print("Press Enter key to continue...")
	input()

class PrintToConsole():
	def __init__(self, printdata, color):
		self.printdata = printdata
		self.color = color
		self.printincolor()
		print(self.printoutput)
	def printincolor(self):
		if self.color == 'red':
			self.printoutput = bcolors.FAIL + self.printdata + bcolors.ENDC
		else:
			if self.color == 'green':
				self.printoutput = bcolors.OKGREEN + self.printdata + bcolors.ENDC
			else:
				self.printoutput = self.printdata

#print(bcolors.HEADER + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
#print(f"{bcolors.WARNING}Starting UP: Continue?{bcolors.ENDC}")

pause()

print_format_table()

pause()

prnt = input("input any to start: ")
PrintToConsole(prnt, "red")

pause()

#SayHello
hello1 = HelloName.hello()
PrintToConsole(hello1, "red")

pause()

#WhatDay
date = '03 03 2021' #this is the input date
PrintToConsole("Today is: " + findDay(date), "green") # here we print the final output after calling the fucntion findday
#CurrentTime
timestring = strftime('%H:%M:%S %p')
PrintToConsole("Current Time is: " + timestring, "green")

pause()

i = int(0)
while i < 1:
	#create object Laptop
		laptop1 = Laptop()
		laptop1.name = 'Dell Alienware'
		laptop1.processor = 'Intel Core i7'
		laptop1.start()
		laptop1.details()
		i = i + 1

pause()

Getip1 = Getip()
PrintToConsole("IP Info: ", 'none')
PrintToConsole(Getip1.wan_ip, 'red')
PrintToConsole(Getip1.lan_ip, 'red')

pause()

Int1 = Int()
Int1.read()
Int1.write()

pause()

#if __name__ == '__main__':
# DO NOT USE IP
host_name = input("host name ? (example github.com) \n")
prt = input("port ? \n")
tcp_it = "https"
#ServHealthCheck
serverHealthCheck = ServerHealthCheck(host_name, prt, tcp_it)
#UrlopenHost
url_path1 = "http" + "://" + host_name
'''
try:
	req1 = Request(url_path1)
	#x = urlopen('http://www.google.com/search?q=test')
	#req = Request(hst)
	x = urlopen(req1)
	print(x.read())
	print("\n")
except Exception as e:
	print(str(e))
	print("\n")
'''

pause()

PrintToConsole('Press ENTER to start StopWatch, Press Ctrl + C to stop')
while True:
	try:
		input()  # For ENTER. Use raw_input() if you are running python 2.x instead of input()
		starttime = time.time()
		PrintToConsole('Started')
		while True:
			PrintToConsole('Time Elapsed: ', round(time.time() - starttime, 0), 'secs', end="\r")
			time.sleep(1) # 1 second delay
		input()
	except: #except KeyboardInterrupt:
		PrintToConsole('Stopped')
		endtime = time.time()
		TotalTimeElapsed = str(round(endtime - starttime, 2)) + 'secs'
		PrintToConsole('Total Time: ' + TotalTimeElapsed)
		break

pause()

WriteToFile.write()

pause()

'''
while True:
	print("Writing info to sample.txt")
	print("File sample.txt is opened.")
#OpenFileToWriteOutput
	text_file = open("2output.txt", "w+") #instead of "wt"
#Hello
	n = text_file.write(hello1)
	n = text_file.write("\n")
	n = text_file.write("\n")
#DateTime
	n = text_file.write("Current Time is: ")
	n = text_file.write(timestring)
	n = text_file.write("\n")
	n = text_file.write("\n")
#Laptop
	n = text_file.write("Your Laptop is: ")
	n = text_file.write(laptop1.name)
	n = text_file.write(" ")
	n = text_file.write(laptop1.processor)
	n = text_file.write("\n")
	n = text_file.write("\n")
#NubersCompare (Int Class)
	n = text_file.write("Your numbers are: ")
	n = text_file.write(str(Int1.n1))
	n = text_file.write(" and ")
	n = text_file.write(str(Int1.n2))
	n = text_file.write(" ")
	n = text_file.write("Comparison: ")
	n = text_file.write(str(Int1.CResult))
	n = text_file.write("\n")
	n = text_file.write("\n")
#UrlopenHost
	n = text_file.write("Your host is: ")
	n = text_file.write(host_name)
	n = text_file.write("\n")
#SiteHealthCheckResults
	n = text_file.write(serverHealthCheck.SHCLog)
	n = text_file.write("\n")
	n = text_file.write("\n")
	#StopWatchStats
	n = text_file.write('Total Time: ')
	n = text_file.write(str(round(endtime - starttime, 2)))
	n = text_file.write(' secs')
	n = text_file.write("\n")
	n = text_file.write("\n")
#CloseFile
	text_file.close()
	print("File sample.txt is closed.")
	print("File sample.txt successfully updated!")

wan_ip = Getip.get_wan_ip()
lan_ip = Getip.get_local_ip()

##open file
#f = open("sample.txt", "x")
##close file
#f.close
#text_file = open("sample.txt", "w")
#n = text_file.write('Welcome to python')
#text_file.close()
#
with open(filename, 'a') as f:
    print(var, file=f)
#OR#
with open('2output.txt', 'a') as out:
    out.write(var + '\n')
#OR#
	#ALTFile for serverHealthCheck
text_file2 = open("SHC.txt", "wt")
text_file2.write(serverHealthCheck.SHCLog)
text_file2.close()
'''

